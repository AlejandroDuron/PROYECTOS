----------------------------------------------------------------------------------------------------------
---- Equipo: The basaboost
----Estudiantes: 
--Kathleen Abigail Argueta Gómez
--Alejandro Javier Durón Rodríguez
--Lorena Esmeralda Mejía Ramos
--Reina Arely Sosa Mejía
--Iván Alessandro Vásquez Martínez
----------------------------------------------------------------------------------------------------------

--- Para conectar a la base de datos:
USE veterinaria;

-------Resolución de ejercicios de la guía-------

-- Ejercicio 1 --
----Muestre el porcentaje de receta que tiene cada medicamento
select
    m.idMedicamento, m.nombre,
    format(
		count(r.idMedicamento) * 1.0 / (select count(*) from receta),
        'N10' -- para mostrar solo 10 decimales
        )
	as PorcentajeUso -- Nombre de la columna creada
from
    medicamento m
join
    receta r on m.idMedicamento = r.idMedicamento -- Une las tablas donde están las cantidades donde están los nombres
group by
    m.idMedicamento, m.nombre;

----------------------------------------------------------------------------------------------------------
-- Ejercicio 2 --
----Basado en el ejercicio anterior, establezca un formato adecuado para mostrar el porcentaje de receta de
----cada medicamento
select
    m.idMedicamento, m.nombre,
    concat(
        format(
            count(r.idMedicamento) * 1.0 / (select count(*) from receta),
            'N2' -- para mostrar solo dos decimales
        ),
        '%' -- para ponerle el símbolo de porcentaje
    ) as PorcentajeUso -- nombre de la columna creada
from
    medicamento m
join
    receta r on m.idMedicamento = r.idMedicamento
group by
    m.idMedicamento, m.nombre;

----------------------------------------------------------------------------------------------------------
-- Ejercicio 3 --
----Mostrar el precio total de cada consulta basándose en la siguiente formula: ((precio de la consulta + IVA) + 
--- (suma de precios de los medicamentos recetados en la consulta)) donde exista al menos 1 medicamento recetado

Select
	c.idConsulta,
	cast(
		( (c.precioConsulta + (c.precioConsulta *0.13)) + sum(m.precio))as decimal (5, 2)
		) as precioConsulta
from
	consulta c
inner join 
	receta r on c.idConsulta = r.idConsulta
inner join 
	medicamento m on m.idMedicamento = r.idMedicamento
group by 
	c.idConsulta, c.precioConsulta;
--En este ejercicio no es necesario poner un validador para ver si hay al menos un medicamento 
--recetado, ya que los inner joins se encargan de eso. 
-- El INNER JOIN garantiza que solo se incluyan consultas con medicamentos recetados.

----------------------------------------------------------------------------------------------------------
-- Ejercicio 3.1 --
----Mostrar el precio total de cada consulta basándose en la siguiente formula: 
----((precio de la consulta + IVA) + (suma de precios de los medicamentos recetados en la consulta)) 
----y ahora todas las consultas, tengan o no tengan medicamentos recetados 

Select c.idConsulta,
	cast(
		(c.precioConsulta + (c.precioConsulta *0.13) + 
			CASE 
				when SUM(m.precio) IS NULL 
			THEN 
				0 else SUM(m.precio) END
         ) AS DECIMAL(10, 2)
		) AS precioTotal 
from consulta c
LEFT JOIN 
	receta r on c.idConsulta = r.idConsulta
LEFT JOIN
	medicamento m on m.idMedicamento = r.idMedicamento
group by
	c.idConsulta, c.precioConsulta
;

----------------------------------------------------------------------------------------------------------
-- Ejercicio 4 --
---- Mostrar el precio de la consulta promedio de cada cliente. Se debe incluir el IVA al precio de la consulta:
----((precio de la consulta + IVA) + (suma de precios de los medicamentos)) donde exista al menos una
---- medicina recetada.

select 
    sub.idCliente, sub.nombreCliente,
    CAST(
		AVG(sub.precioTotal) as decimal(10,2)
		) as "Precio promedio por consulta"
from (
    select 
        cliente.idCliente,
        cliente.nombreCliente,
        consulta.idConsulta,
        (consulta.precioConsulta * 1.13) + sum(medicamento.precio) as precioTotal
    from cliente
    join paciente on cliente.idCliente = paciente.idCliente
    join consulta on paciente.idPaciente = consulta.idPaciente
    join receta on consulta.idConsulta = receta.idConsulta
    join medicamento on receta.idMedicamento = medicamento.idMedicamento
    group by cliente.idCliente, cliente.nombreCliente, consulta.idConsulta, consulta.precioConsulta
) as sub
group by sub.idCliente, sub.nombreCliente;

----------------------------------------------------------------------------------------------------------
-- Ejercicio 4.1 --
----Mostrar el precio de la consulta promedio de cada cliente. Se debe incluir el IVA al precio de la
----consulta: ((precio de la consulta + IVA) + (suma de precios de los medicamentos)) donde puede haber
----o no medicamento recetado

select 
    sub.idCliente,
    sub.nombreCliente,
    CAST(
		ROUND(
			AVG(sub.precioTotal), 2
			)
		as decimal(10,2)
		) as "Precio promedio por consulta"
from (
    select 
        cliente.idCliente,
        cliente.nombreCliente,
        consulta.idConsulta,
        (consulta.precioConsulta * 1.13) + ISNULL(sum(medicamento.precio), 0) as precioTotal
    from cliente
    join paciente on cliente.idCliente = paciente.idCliente
    join consulta on paciente.idPaciente = consulta.idPaciente
    left join receta on consulta.idConsulta = receta.idConsulta
    left join medicamento on receta.idMedicamento = medicamento.idMedicamento
    group by cliente.idCliente, cliente.nombreCliente, consulta.idConsulta, consulta.precioConsulta
) as sub
group by sub.idCliente, sub.nombreCliente;

----------------------------------------------------------------------------------------------------------
-- Ejercicio 5 --
----Realizar una consulta que muestre la ganancia de la veterinaria entre marzo y mayo de 2024. Tomar en
----cuenta las consultas y las medicinas recetadas. NOTA: en la tabla consulta solo hay registros de 2024

select 
    DATENAME(MONTH, c.fecha) as mes,
    CAST(
		ROUND(
			SUM(
				(c.precioConsulta * 1.13) + medicinas.totalMedicinas), 2
			) as decimal (10,2)
		) as ganancias
from 
    consulta c
left join 
    (
        select 
            r.idConsulta,
            SUM(m.precio) as totalMedicinas
        from 
            receta r
        left join 
            medicamento m on r.idMedicamento = m.idMedicamento
        group by 
            r.idConsulta
    ) medicinas on c.idConsulta = medicinas.idConsulta
where 
     c.fecha >= CONVERT(date, '01/03/2024 00:00:00', 103)
     AND c.fecha <= CONVERT(date, '31/05/2024 00:00:00', 103)
group by 
    MONTH(c.fecha),
	DATENAME(MONTH, c.fecha)
	
----------------------------------------------------------------------------------------------------------
-- Ejercicio 6 --
---- Agregar una columna descuento a la tabla medicamento y realice una sola. Consulta para poder actualizar
----esta columna con el precio del medicamento con un 5% de descuento. Aplicar este descuento únicamentea
----los productos que hayan sido recetados en 3 o menos consultas.

Select 
	m.idMedicamento, 
	m.nombre, 
	m.precio, 
	case
		when qConsultas.cantidad >= 3 then Cast((m.precio*0.95) as decimal (10,2))
		else Null
	end as descuento 
From
	medicamento m
left join 
			(Select 
					r.idMedicamento, COUNT(r.idMedicamento) as cantidad
				From 
					receta r
				Group by 
					r.idMedicamento
				Having 
					COUNT(r.idMedicamento) >= 3) as qConsultas
On m.idMedicamento = qConsultas.idMedicamento

----------------------------------------------------------------------------------------------------------
-- Ejercicio 7 --
---- Mostrar el porcentaje de consultas atendidas por cada veterinario entre los meses marzo y abril de 2024

select
    m.idMedico,
    m.nombreMedico,
    -- Para el conteo de consultas que el médico atendió en el periodo:
    count(c.idConsulta) as ConsultasEnPeriodo,
    -- Para agregar el porcentaje en formato decimal:
    CAST(
        COUNT(c.idConsulta) * 1.0 / (
            select count(*) from consulta
            where fecha BETWEEN '2024-03-01' AND '2024-04-30'
			) as decimal(5,2)
		) as porcentajeConsultas
from medico as m
inner join consulta as c
    on m.idMedico = c.idMedico
where c.fecha BETWEEN '2024-03-01' AND '2024-04-30'
group by
    m.idMedico,
    m.nombreMedico
order by
    m.idMedico;

----------------------------------------------------------------------------------------------------------
-- Ejercicio 8 --
---- Calcular el bono de medio año para cada doctor veterinario, la forma de cálculo es la siguiente:
---- 2 años o menos		50% del salario actual
---- >2 y <5			75% del salario actual
---- =>5				100% del salario actual
---- NOTA: hacer el calculo de diferencia de años con el año actual.

select
    idMedico, nombreMedico, salario, FechaContrato,
    -- Para calcular los años de servicio con fechas y años: 
    DATEDIFF(YEAR, FechaContrato, GETDATE() 
			) AS añosTrabajo,
    -- Acá se determinan los años trabajados:
    case
        when DATEDIFF(YEAR, FechaContrato, GETDATE()) <= 2
            then salario * 0.50
        when DATEDIFF(YEAR, FechaContrato, GETDATE()) > 2
             and DATEDIFF(YEAR, FechaContrato, GETDATE()) < 5
            then salario * 0.75
        else 
            salario
    end as bono
from medico
order by idMedico;