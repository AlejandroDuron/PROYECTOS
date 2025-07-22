namespace _Arbol_AVL
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label1 = new System.Windows.Forms.Label();
            this.valor = new System.Windows.Forms.TextBox();
            this.btnSalir = new System.Windows.Forms.Button();
            this.btnEliminar = new System.Windows.Forms.Button();
            this.btnBuscar = new System.Windows.Forms.Button();
            this.btnAgregar = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.rbPostOrden = new System.Windows.Forms.RadioButton();
            this.rbEnOrden = new System.Windows.Forms.RadioButton();
            this.rbPreOrden = new System.Windows.Forms.RadioButton();
            this.txtRecorrido = new System.Windows.Forms.TextBox();
            this.lblAltura = new System.Windows.Forms.Label();
            this.errores = new System.Windows.Forms.ErrorProvider(this.components);
            this.lblTipo = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.errores)).BeginInit();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.valor);
            this.groupBox1.Controls.Add(this.btnSalir);
            this.groupBox1.Controls.Add(this.btnEliminar);
            this.groupBox1.Controls.Add(this.btnBuscar);
            this.groupBox1.Controls.Add(this.btnAgregar);
            this.groupBox1.ForeColor = System.Drawing.SystemColors.ControlText;
            this.groupBox1.Location = new System.Drawing.Point(1074, 132);
            this.groupBox1.Margin = new System.Windows.Forms.Padding(9);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Padding = new System.Windows.Forms.Padding(20);
            this.groupBox1.Size = new System.Drawing.Size(200, 311);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(47, 26);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(104, 25);
            this.label1.TabIndex = 5;
            this.label1.Text = "Opciones";
            // 
            // valor
            // 
            this.valor.Location = new System.Drawing.Point(24, 83);
            this.valor.Name = "valor";
            this.valor.Size = new System.Drawing.Size(153, 22);
            this.valor.TabIndex = 4;
            // 
            // btnSalir
            // 
            this.btnSalir.Location = new System.Drawing.Point(23, 251);
            this.btnSalir.Name = "btnSalir";
            this.btnSalir.Size = new System.Drawing.Size(153, 37);
            this.btnSalir.TabIndex = 3;
            this.btnSalir.Text = "Salir";
            this.btnSalir.UseVisualStyleBackColor = true;
            this.btnSalir.Click += new System.EventHandler(this.btnSalir_Click);
            // 
            // btnEliminar
            // 
            this.btnEliminar.Location = new System.Drawing.Point(24, 208);
            this.btnEliminar.Name = "btnEliminar";
            this.btnEliminar.Size = new System.Drawing.Size(153, 37);
            this.btnEliminar.TabIndex = 2;
            this.btnEliminar.Text = "Eliminar Dato";
            this.btnEliminar.UseVisualStyleBackColor = true;
            this.btnEliminar.Click += new System.EventHandler(this.btnEliminar_Click);
            // 
            // btnBuscar
            // 
            this.btnBuscar.Location = new System.Drawing.Point(24, 165);
            this.btnBuscar.Name = "btnBuscar";
            this.btnBuscar.Size = new System.Drawing.Size(153, 37);
            this.btnBuscar.TabIndex = 1;
            this.btnBuscar.Text = "Buscar Dato";
            this.btnBuscar.UseVisualStyleBackColor = true;
            this.btnBuscar.Click += new System.EventHandler(this.btnBuscar_Click);
            // 
            // btnAgregar
            // 
            this.btnAgregar.Location = new System.Drawing.Point(23, 122);
            this.btnAgregar.Name = "btnAgregar";
            this.btnAgregar.Size = new System.Drawing.Size(153, 37);
            this.btnAgregar.TabIndex = 0;
            this.btnAgregar.Text = "Agregar Dato";
            this.btnAgregar.UseVisualStyleBackColor = true;
            this.btnAgregar.Click += new System.EventHandler(this.btnAgregar_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.rbPostOrden);
            this.groupBox2.Controls.Add(this.rbEnOrden);
            this.groupBox2.Controls.Add(this.rbPreOrden);
            this.groupBox2.Controls.Add(this.txtRecorrido);
            this.groupBox2.Location = new System.Drawing.Point(201, 517);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(905, 100);
            this.groupBox2.TabIndex = 1;
            this.groupBox2.TabStop = false;
            // 
            // rbPostOrden
            // 
            this.rbPostOrden.AutoSize = true;
            this.rbPostOrden.Location = new System.Drawing.Point(781, 21);
            this.rbPostOrden.Name = "rbPostOrden";
            this.rbPostOrden.Size = new System.Drawing.Size(94, 20);
            this.rbPostOrden.TabIndex = 8;
            this.rbPostOrden.TabStop = true;
            this.rbPostOrden.Text = "Post-orden";
            this.rbPostOrden.UseVisualStyleBackColor = true;
            this.rbPostOrden.CheckedChanged += new System.EventHandler(this.rbPostOrden_CheckedChanged);
            // 
            // rbEnOrden
            // 
            this.rbEnOrden.AutoSize = true;
            this.rbEnOrden.Location = new System.Drawing.Point(421, 21);
            this.rbEnOrden.Name = "rbEnOrden";
            this.rbEnOrden.Size = new System.Drawing.Size(77, 20);
            this.rbEnOrden.TabIndex = 7;
            this.rbEnOrden.TabStop = true;
            this.rbEnOrden.Text = "In-orden";
            this.rbEnOrden.UseVisualStyleBackColor = true;
            this.rbEnOrden.CheckedChanged += new System.EventHandler(this.rbEnOrden_CheckedChanged);
            // 
            // rbPreOrden
            // 
            this.rbPreOrden.AutoSize = true;
            this.rbPreOrden.Location = new System.Drawing.Point(17, 21);
            this.rbPreOrden.Name = "rbPreOrden";
            this.rbPreOrden.Size = new System.Drawing.Size(88, 20);
            this.rbPreOrden.TabIndex = 4;
            this.rbPreOrden.TabStop = true;
            this.rbPreOrden.Text = "Pre-orden";
            this.rbPreOrden.UseVisualStyleBackColor = true;
            this.rbPreOrden.CheckedChanged += new System.EventHandler(this.rbPreOrden_CheckedChanged);
            // 
            // txtRecorrido
            // 
            this.txtRecorrido.Location = new System.Drawing.Point(17, 63);
            this.txtRecorrido.Name = "txtRecorrido";
            this.txtRecorrido.Size = new System.Drawing.Size(867, 22);
            this.txtRecorrido.TabIndex = 6;
            // 
            // lblAltura
            // 
            this.lblAltura.AutoSize = true;
            this.lblAltura.Location = new System.Drawing.Point(1161, 30);
            this.lblAltura.Name = "lblAltura";
            this.lblAltura.Size = new System.Drawing.Size(113, 16);
            this.lblAltura.TabIndex = 6;
            this.lblAltura.Text = "Altura del arbol:  #";
            // 
            // errores
            // 
            this.errores.ContainerControl = this;
            // 
            // lblTipo
            // 
            this.lblTipo.AutoSize = true;
            this.lblTipo.Location = new System.Drawing.Point(1071, 89);
            this.lblTipo.Name = "lblTipo";
            this.lblTipo.Size = new System.Drawing.Size(167, 16);
            this.lblTipo.TabIndex = 7;
            this.lblTipo.Text = "Tipo de rotacion realizada:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.ClientSize = new System.Drawing.Size(1330, 651);
            this.Controls.Add(this.lblTipo);
            this.Controls.Add(this.lblAltura);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.errores)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button btnSalir;
        private System.Windows.Forms.Button btnEliminar;
        private System.Windows.Forms.Button btnBuscar;
        private System.Windows.Forms.Button btnAgregar;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox valor;
        private System.Windows.Forms.TextBox txtRecorrido;
        private System.Windows.Forms.RadioButton rbPostOrden;
        private System.Windows.Forms.RadioButton rbEnOrden;
        private System.Windows.Forms.RadioButton rbPreOrden;
        private System.Windows.Forms.Label lblAltura;
        private System.Windows.Forms.ErrorProvider errores;
        private System.Windows.Forms.Label lblTipo;
    }
}

