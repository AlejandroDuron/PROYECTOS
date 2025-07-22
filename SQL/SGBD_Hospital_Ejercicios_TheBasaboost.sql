use SG_Hospital_TheBasaboost

;
--###################################################################################################

-- SEGURIDAD DE LA BASE
CREATE SCHEMA seguridad;

-- Log Ins

CREATE LOGIN loginMedico 
WITH PASSWORD = 'Ale1234';

CREATE LOGIN loginRecepcion 
WITH PASSWORD = 'Andre12';


-- Usuarios 
CREATE USER usuario_medico
FOR LOGIN loginMedico 
WITH DEFAULT_SCHEMA = seguridad;

CREATE USER usuario_recepcion
FOR LOGIN loginRecepcion 
WITH DEFAULT_SCHEMA = seguridad;

--###################################################################################################

-- *Triggers:

-- 1. Actualizar automáticamente el estado de una cita al registrar una consulta. 
DROP TRIGGER IF EXISTS trg_ActualizarEstadoCita;
CREATE TRIGGER trg_ActualizarEstadoCita
ON CONSULTA
AFTER INSERT
AS
BEGIN
    UPDATE CITA
    SET id_estado = (SELECT id_estado FROM ESTADO_CITA WHERE estado = 'Atendida')
    WHERE id_cita IN (SELECT id_cita FROM INSERTED);
END;

-- 2. Validar que un médico no tenga citas al mismo tiempo. 
CREATE TRIGGER trg_validar_cita_medico
ON CITA
INSTEAD OF INSERT
AS
BEGIN
    -- Verificar si el médico ya tiene una cita en la misma fecha y hora
    IF EXISTS (
        SELECT 1
        FROM CITA c
        JOIN INSERTED i
            ON c.id_medico = i.id_medico
            AND c.fecha_hora = i.fecha_hora
    )
    BEGIN
        RAISERROR('El médico ya tiene una cita registrada a esa hora.', 16, 1);
        RETURN;
    END

    -- Sino insertar la cita
    INSERT INTO CITA (id_paciente, id_medico, id_estado, fecha_hora)
    SELECT id_paciente, id_medico, id_estado, fecha_hora
    FROM INSERTED;
END;

-- 3. Registrar en log cuando una cita se cancela.
-- Se crea tabla que recibira las citas canceladas para permitir la recuperacion de datos

CREATE TABLE LOG_CITAS_CANCELADAS (
    id_log INT PRIMARY KEY IDENTITY,
    id_cita INT,
    id_paciente INT,
    id_medico INT,
    estado_cita VARCHAR(15),
    fecha_hora DATETIME,
    motivo_cancelacion VARCHAR(255),
    fecha_cancelacion DATETIME DEFAULT GETDATE()
);

CREATE TRIGGER TRG_LOG_CITA_CANCELADA
ON CITA
AFTER UPDATE
AS
BEGIN
    -- Verificar si el estado cambió a 'Cancelada' (id_estado = 3)
    IF EXISTS (SELECT 1 FROM inserted WHERE id_estado = 3) AND NOT EXISTS (SELECT 1 FROM deleted WHERE id_estado = 3)
    BEGIN
        -- Insertar en el log de citas canceladas
        INSERT INTO LOG_CITAS_CANCELADAS (
            id_cita, id_paciente, id_medico, estado_cita, fecha_hora, motivo_cancelacion
        )
        SELECT 
            i.id_cita, 
            i.id_paciente, 
            i.id_medico, 
            'Cancelada', 
            i.fecha_hora, 
            'Cita cancelada por el paciente o el médico'
        FROM inserted i;
    END
END;

-- EJEMPLO
UPDATE CITA 
SET id_estado = 3 
WHERE id_cita = 1;

-- Se activo el trigger correctamente si hay datos
SELECT * FROM LOG_CITAS_CANCELADAS;

--##############################################################################################################

-- *Procedimientos almacenados:

-- 1. Registrar una nueva cita. 
DROP PROCEDURE IF EXISTS seguridad.registro_cita;
CREATE PROCEDURE seguridad.registro_cita
	@id_paciente INT,
	@id_medico SMALLINT,
	@id_estado SMALLINT,
	@fecha_hora DATETIME
AS
BEGIN
	INSERT INTO CITA(id_paciente, id_medico, id_estado, fecha_hora) VALUES
	(@id_paciente, @id_medico, @id_estado, @fecha_hora);
END;

-- Estos son datos de prueba, puede intentar con otros datos si lo prefiere
EXEC seguridad.registro_cita @id_paciente = 3, @id_medico = 16, 
	@id_estado = 1, @fecha_hora = '2023-07-10 13:00:00';

--Consultas para tener una guia de los datos que se pueden poner en el procedimiento almacenado
SELECT * FROM PACIENTE;
SELECT * FROM MEDICO;
SELECT * FROM ESPECIALIDAD;
SELECT * FROM ESTADO_CITA;
SELECT * FROM CITA;

-- 2.Registrar una consulta médica. 
SELECT * FROM CONSULTA;
SELECT * FROM DIAGNOSTICO;

DROP PROCEDURE IF EXISTS seguridad.registro_consulta;
CREATE PROCEDURE seguridad.registro_consulta
	@id_cita INT,
	@id_diagnostico SMALLINT,
	@observaciones VARCHAR(250),
	@fecha DATE
AS
BEGIN
	INSERT INTO CONSULTA(id_cita, id_diagnostico, observaciones, fecha_consulta) VALUES
	(@id_cita, @id_diagnostico, @observaciones, @fecha);
END;

-- Estos son datos de prueba, puede intentar con otros datos si lo prefiere
EXEC seguridad.registro_consulta @id_cita = 66, @id_diagnostico = 3, @observaciones = 'Sintomas no severos', @fecha = '2023-07-10';


-- 3. Generar una receta para una consulta. 
DROP PROCEDURE IF EXISTS seguridad.receta_consulta;
CREATE PROCEDURE seguridad.receta_consulta
	@id_consulta INT,
	@id_medicamento INT,
	@dosis VARCHAR(50),
	@duracion VARCHAR(50),
	@instrucciones VARCHAR(100)
AS
BEGIN
	INSERT INTO RECETA(id_consulta, id_medicamento, dosis, duracion, instrucciones) VALUES
	(@id_consulta, @id_medicamento, @dosis, @duracion, @instrucciones);
END;

EXEC receta_consulta @id_consulta = 66, @id_medicamento = 3, @dosis = '10 mg', @duracion = 'Cada 12 horas x 6 dias', @instrucciones = 'Tomar despues de comer';

SELECT * FROM MEDICAMENTO;
SELECT * FROM RECETA;

-- 4.Buscar pacientes por nombre o DUI. 
DROP PROCEDURE IF EXISTS seguridad.buscar_paciente_DUI;
CREATE PROCEDURE seguridad.buscar_paciente_DUI
	@dui VARCHAR(10)
AS
BEGIN
	SELECT * 
	FROM PACIENTE p
	WHERE p.dui = @dui
END;

--DUI de prueba
EXEC seguridad.buscar_paciente_DUI @dui = '04567890-1';

--Para ver mas DUIs rapido
SELECT P.id_paciente, P.nombre, P.apellido, P.dui FROM PACIENTE P;

-- 5. ver las citas activas por paciente
Create procedure seguridad.ver_citas_activas

---- estos son los parametros que puede utilizar
    @id_paciente int = null,
    @id_cita int = null
as
begin
-- primero actualizar citas de prueba a fechas futuras (a modo de ejemplo)
    update top (10) cita 
    set fecha_hora = dateadd(day, 7, getdate()),
        id_estado = case when id_estado = 2 then 1 else id_estado end
    where id_cita in (1, 2, 5, 10, 15, 20, 25, 30, 35, 40);
    select 
	--- se usan '' por el espacio que hay entre los nombres y no genere error
        c.id_cita,
        p.nombre + ' ' + p.apellido as paciente,
        p.dui,
        m.nombre + ' ' + m.apellido as medico,
        e.especialidad,
        ec.estado as estado_cita,
        c.fecha_hora,
        datediff(hour, getdate(), c.fecha_hora) as horas_restantes
    from 
       cita c
        inner join paciente p on c.id_paciente = p.id_paciente
        inner join medico m on c.id_medico = m.id_medico
        inner join especialidad e on m.id_especialidad = e.id_especialidad
        inner join estado_cita ec on c.id_estado = ec.id_estado
    where 
	-- 1 significa pendiente y 5 urgente. a modo de ejemplo, claro.             
/*1. pendiente
  2. atendida
  3. cancelada
  4.reprogramada
  5. urgente*/
        (c.id_estado = 1 or c.id_estado = 5)  -- 1=pendiente, 5=urgente
        and (@id_paciente is null or c.id_paciente = @id_paciente)
        and (@id_cita is null or c.id_cita = @id_cita)
        and c.fecha_hora > getdate()
    order by 
        c.fecha_hora asc;
end;

--- aquí se muestra el ejemplo de su funcionamiento, con datos de prueba. 
---- en las inserciones puede verificar e indicar cuál desea consultar.

-- visualizar todas las citas activas
exec seguridad.ver_citas_activas;

-- ver citas por paciente
exec seguridad.ver_citas_activas @id_paciente = 1;

-- ver cita en especifíco
exec seguridad.ver_citas_activas @id_cita = 5;

--########################################################################################################

--- Vistas

--- 1. Agenda diaria de un médico
create view seguridad.vista_agenda_medica_diaria as
--- Estados de cita que incluímos por defecto:
  ---1. Pendiente
  ---2. Atendida
select 
    m.id_medico,
    m.nombre + ' ' + m.apellido as medico,
    e.especialidad,
    convert(varchar, c.fecha_hora, 23) as fecha,  
    c.id_cita,
    convert(varchar, c.fecha_hora, 108) as hora,  
    p.nombre + ' ' + p.apellido as paciente,
    p.dui,
    p.telefono as telefono_paciente,
    ec.estado as estado_cita
from 
    medico m
    INNER JOIN cita c on m.id_medico = c.id_medico
    INNER JOIN paciente p on c.id_paciente = p.id_paciente
    INNER JOIN especialidad e on m.id_especialidad = e.id_especialidad
    INNER JOIN estado_cita ec on c.id_estado = ec.id_estado
where 
    c.id_estado IN (1, 2)  
    AND c.fecha_hora >= cast(getdate() as date);

-----Ejemplos para que pueda probar:
-- Ver agenda completa
select * from seguridad.vista_agenda_medica_diaria;

-- Agenda de un médico en específico
select * from seguridad.vista_agenda_medica_diaria 
where id_medico = 23 AND estado_cita = 'Pendiente';


---- 2. historial clínico detallado de pacientes
CREATE seguridad.vista_historial_clinico AS
SELECT 
    p.id_paciente,
    p.nombre + ' ' + p.apellido AS paciente_completo,
    p.dui,
    p.fecha_nacimiento,
    DATEDIFF(YEAR, p.fecha_nacimiento, GETDATE()) AS edad,
    p.direccion,
    p.telefono,
    p.email,

    -- Alergias: concatenar todas las alergias del historial médico
    ISNULL((
        SELECT STRING_AGG(a.alergias, ', ')
        FROM historial_medico hm2
        INNER JOIN historial_alergias ha ON hm2.id_historial_medico = ha.id_historial_medico
        INNER JOIN alergias a ON ha.id_alergias = a.id_alergias
        WHERE hm2.id_paciente = p.id_paciente
    ), 'ninguna registrada') AS alergias,

    -- Enfermedades crónicas: concatenar todas las enfermedades del historial médico
    ISNULL((
        SELECT STRING_AGG(ec.enfermedad_cronica, ', ')
        FROM historial_medico hm3
        INNER JOIN HISTORIAL_ENF_CRONICAS he ON hm3.id_historial_medico = he.id_enfermedades_cronicas
        INNER JOIN enfermedades_cronicas ec ON he.id_enfermedades_cronicas = ec.id_enfermedades_cronicas
        WHERE hm3.id_paciente = p.id_paciente
    ), 'ninguna registrada') AS enfermedades_cronicas,

    -- Antecedentes familiares
    hm.antecedentes_familiares,

    -- Últimas consultas
    STUFF((
        SELECT ', ' + CONVERT(VARCHAR, c.fecha_hora, 103) + ' - ' + d.diagnostico
        FROM consulta co
        INNER JOIN cita c ON co.id_cita = c.id_cita
        INNER JOIN diagnostico d ON co.id_diagnostico = d.id_diagnostico
        WHERE c.id_paciente = p.id_paciente
        ORDER BY c.fecha_hora DESC
        FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 2, '') AS ultimas_consultas,

    -- Medicamentos recientes
    STUFF((
        SELECT ', ' + me.medicamento + ' (' + r.dosis + ')'
        FROM receta r
        INNER JOIN consulta co ON r.id_consulta = co.id_consulta
        INNER JOIN cita c ON co.id_cita = c.id_cita
        INNER JOIN medicamento me ON r.id_medicamento = me.id_medicamento
        WHERE c.id_paciente = p.id_paciente
        ORDER BY c.fecha_hora DESC
        FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 2, '') AS medicamentos_recetados

FROM 
    paciente p
    LEFT JOIN historial_medico hm ON p.id_paciente = hm.id_paciente;

--- Ejemplos: Se pueden modificar, hay data solo para demostrar su funcionamiento
-- ver el historial de todos los pacientes
select * from seguridad.vista_historial_clinico;
-- ver historial de un paciente específico por id
select * from seguridad.vista_historial_clinico where id_paciente = 1;
-- buscar pacientes con alergias específicas
select * from seguridad.vista_historial_clinico 
where alergias like '%penicilina%';
-- pacientes con enfermedades crónicas
select * from seguridad.vista_historial_clinico
where enfermedades_cronicas = 'ninguna registrada';
-- historial de pacientes mayores de 40 años
select * from seguridad.vista_historial_clinico
where edad > 40;

---- 3. Consultas en el último mes
create view seguridad.vista_consultas_ultimo_mes as
with ultima_fecha as (
    select MAX(fecha_consulta) as max_fecha 
    from consulta
)
select 
    c.id_consulta,
    format(c.fecha_consulta, 'dd/MM/yyyy') as fecha_consulta,
    p.nombre + ' ' + p.apellido AS paciente,
    p.dui,
    m.nombre + ' ' + m.apellido AS medico,
    e.especialidad,
    d.diagnostico,
    c.observaciones,
    string_agg(me.medicamento + ' (' + r.dosis + ')', ', ') as medicamentos_recetados
from 
    consulta c
    INNER JOIN cita ci on c.id_cita = ci.id_cita
    INNER JOIN paciente p on ci.id_paciente = p.id_paciente
    INNER JOIN medico m on ci.id_medico = m.id_medico
    INNER JOIN especialidad e ON m.id_especialidad = e.id_especialidad
    INNER JOIN diagnostico d on c.id_diagnostico = d.id_diagnostico
    LEFT JOIN receta r on c.id_consulta = r.id_consulta
    LEFT JOIN medicamento me on r.id_medicamento = me.id_medicamento
    CROSS JOIN ultima_fecha uf
where 
    -- Ultimo mes
    c.fecha_consulta >= dateadd(month, -1, uf.max_fecha)
    AND c.fecha_consulta <= uf.max_fecha
group by
    c.id_consulta,
    c.fecha_consulta,
    p.nombre,
    p.apellido,
    p.dui,
    m.nombre,
    m.apellido,
    e.especialidad,
    d.diagnostico,
    c.observaciones;

----Ejemplos:
-- ver todas las consultas del último mes
select * from seguridad.vista_consultas_ultimo_mes; --- Muy gracioso, solo hay 1 jaja

---- 4. Medicamentos recetados por diágnostico
create view seguridad.vista_medicamentos_diagnosticos as
select 
    r.id_receta,
    m.medicamento,
    r.dosis,
    r.duracion,
    r.instrucciones,
    d.diagnostico,
    p.nombre + ' ' + p.apellido as paciente,
    p.dui,
    med.nombre + ' ' + med.apellido as médico_a_cargo,
    e.especialidad,
    format(c.fecha_consulta, 'dd/mm/yyyy') as fecha_consulta
from 
    receta r
    inner join medicamento m on r.id_medicamento = m.id_medicamento
    inner join consulta c on r.id_consulta = c.id_consulta
    inner join diagnostico d on c.id_diagnostico = d.id_diagnostico
    inner join cita ci on c.id_cita = ci.id_cita
    inner join paciente p on ci.id_paciente = p.id_paciente
    inner join medico med on ci.id_medico = med.id_medico
    inner join especialidad e on med.id_especialidad = e.id_especialidad;

-- ver todos los medicamentos recetados por diagnósticos
select * from seguridad.vista_medicamentos_diagnosticos;


---- 5. Ranking de especialidades más consultadas
create view seguridad.vista_ranking_especialidades as
select
    e.especialidad,
    count(c.id_consulta) as total_consultas,
    concat(format(round(count(c.id_consulta) * 100.0 / 
        nullif((select count(*) from consulta), 0), 1), 'n1'), '%') as porcentaje_total
from 
    consulta c
    inner join cita ci on c.id_cita = ci.id_cita
    inner join medico m on ci.id_medico = m.id_medico
    inner join especialidad e on m.id_especialidad = e.id_especialidad
group by 
    e.especialidad;

--- Se puede probar asi:
select * from seguridad.vista_ranking_especialidades 
order by total_consultas desc;


--- 6. Ranking de medicinas mas recetadas
create view seguridad.vista_ranking_medicinas_recetadas as
select
    m.medicamento,
    count(r.id_receta) as total_recetas,
    concat(format(round(count(r.id_receta) * 100.0 / 
        nullif((select count(*) from receta), 0), 1), 'N1'), '%') as porcentaje_total
from
    receta r
    inner join medicamento m on r.id_medicamento = m.id_medicamento
group by
    m.medicamento;

--- Se puede probar asi:
select * from seguridad.vista_ranking_medicinas_recetadas
order by total_recetas desc;

--###################################################################################################

-- ASIGNACION DE ROLES

CREATE ROLE rol_medico;
CREATE ROLE rol_recepcion;
CREATE ROLE rol_reportes;

--- PERMISOS
-- ROL MEDICO:

-- Permisos para consultar el historial clínico
GRANT SELECT ON seguridad.vista_historial_clinico TO rol_medico;

-- Permisos para generar recetas
GRANT EXECUTE ON seguridad.receta_consulta TO rol_medico;

-- Permisos para insertar, eliminar y editar recetas
GRANT INSERT, DELETE, UPDATE ON RECETA TO rol_medico;

-- Permisos para registrar consultas médicas
GRANT EXECUTE ON seguridad.registro_consulta TO rol_medico;

-- ROL RECEPCIONISTA:

-- Permisos para CRUD de pacientes
GRANT SELECT, INSERT, UPDATE, DELETE ON PACIENTE TO rol_recepcion;

-- Permisos para ver citas
GRANT SELECT ON seguridad.vista_agenda_medica_diaria TO rol_recepcion

-- Permisos para agendar citas
GRANT EXECUTE ON seguridad.registro_cita TO rol_recepcion;

-- Permisos para CRUD de citas
GRANT SELECT, INSERT, UPDATE, DELETE ON CITA TO rol_recepcion;

-- ROL REPORTES:

-- Permisos para acceder a vistas de estadísticas
GRANT SELECT ON seguridad.vista_ranking_especialidades TO rol_reportes;
GRANT SELECT ON seguridad.vista_ranking_medicinas_recetadas TO rol_reportes;
GRANT SELECT ON seguridad.vista_consultas_ultimo_mes TO rol_reportes;
GRANT SELECT ON seguridad.vista_medicamentos_diagnosticos TO rol_reportes;

-- ASIGNACION DE USUARIOS A SUS ROLES

EXEC sp_addrolemember 'rol_medico', 'usuario_medico';
EXEC sp_addrolemember 'rol_recepcion', 'usuario_recepcion';

--- PRUEBAS DE USUARIOS

-- Para usuario medico:
EXECUTE AS USER = 'usuario_medico';

-- Intentar consultar el historial clínico (debería funcionar)
SELECT * FROM seguridad.vista_historial_clinico;

-- Intentar eliminar un paciente (debería fallar)
DELETE FROM PACIENTE WHERE id_paciente = 1;

-- Intentar generar una receta (debería funcionar)
EXEC seguridad.receta_consulta;

-- Intentar acceder a vistas de reportes (debería fallar)
SELECT * FROM seguridad.vista_ranking_especialidades;

-- Terminar la simulación
REVERT;

-- Para usuario recepcion:
EXECUTE AS USER = 'usuario_recepcion';

-- Intentar registrar una cita (debería funcionar)
EXEC seguridad.registro_cita @id_paciente = 1, @id_medico = 2, @id_estado = 1, @fecha_hora = '2023-07-15 09:00:00';

-- Intentar acceder a diagnósticos (debería fallar)
SELECT * FROM seguridad.vista_medicamentos_diagnosticos;

-- Intentar acceder al historial médico (debería fallar)
SELECT * FROM seguridad.vista_historial_clinico;

-- Intentar ver citas (debería funcionar)
SELECT * FROM seguridad.vista_agenda_medica_diaria;

-- Terminar la simulación
REVERT;
