namespace Arbol_Binario
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
            this.label1 = new System.Windows.Forms.Label();
            this.panel1 = new System.Windows.Forms.Panel();
            this.btnInsertar = new System.Windows.Forms.Button();
            this.btnEliminar = new System.Windows.Forms.Button();
            this.btnBuscar = new System.Windows.Forms.Button();
            this.txtDato = new System.Windows.Forms.TextBox();
            this.txtEliminar = new System.Windows.Forms.TextBox();
            this.txtBuscar = new System.Windows.Forms.TextBox();
            this.btnPre = new System.Windows.Forms.Button();
            this.btnPost = new System.Windows.Forms.Button();
            this.btnEn = new System.Windows.Forms.Button();
            this.lblRecorrido = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.lblCantidad = new System.Windows.Forms.Label();
            this.lblSuma = new System.Windows.Forms.Label();
            this.lblAltura = new System.Windows.Forms.Label();
            this.btnCantidad = new System.Windows.Forms.Button();
            this.btnSuma = new System.Windows.Forms.Button();
            this.btnAltura = new System.Windows.Forms.Button();
            this.btnCargar = new System.Windows.Forms.Button();
            this.btnGuardar = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(530, 40);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(571, 29);
            this.label1.TabIndex = 0;
            this.label1.Text = "Simulador de Arbol Binario de Busqueda (ABB) ";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // panel1
            // 
            this.panel1.Location = new System.Drawing.Point(381, 103);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(924, 425);
            this.panel1.TabIndex = 1;
            this.panel1.Paint += new System.Windows.Forms.PaintEventHandler(this.panel1_Paint);
            // 
            // btnInsertar
            // 
            this.btnInsertar.Location = new System.Drawing.Point(13, 159);
            this.btnInsertar.Name = "btnInsertar";
            this.btnInsertar.Size = new System.Drawing.Size(177, 51);
            this.btnInsertar.TabIndex = 2;
            this.btnInsertar.Text = "Insertar Nodo";
            this.btnInsertar.UseVisualStyleBackColor = true;
            this.btnInsertar.Click += new System.EventHandler(this.btnInsertar_Click);
            // 
            // btnEliminar
            // 
            this.btnEliminar.Location = new System.Drawing.Point(13, 254);
            this.btnEliminar.Name = "btnEliminar";
            this.btnEliminar.Size = new System.Drawing.Size(177, 51);
            this.btnEliminar.TabIndex = 3;
            this.btnEliminar.Text = "Eliminar Nodo";
            this.btnEliminar.UseVisualStyleBackColor = true;
            this.btnEliminar.Click += new System.EventHandler(this.btnEliminar_Click);
            // 
            // btnBuscar
            // 
            this.btnBuscar.Location = new System.Drawing.Point(13, 338);
            this.btnBuscar.Name = "btnBuscar";
            this.btnBuscar.Size = new System.Drawing.Size(177, 51);
            this.btnBuscar.TabIndex = 4;
            this.btnBuscar.Text = "Buscar Nodo";
            this.btnBuscar.UseVisualStyleBackColor = true;
            this.btnBuscar.Click += new System.EventHandler(this.btnBuscar_Click);
            // 
            // txtDato
            // 
            this.txtDato.Location = new System.Drawing.Point(196, 173);
            this.txtDato.Name = "txtDato";
            this.txtDato.Size = new System.Drawing.Size(135, 22);
            this.txtDato.TabIndex = 5;
            // 
            // txtEliminar
            // 
            this.txtEliminar.Location = new System.Drawing.Point(196, 268);
            this.txtEliminar.Name = "txtEliminar";
            this.txtEliminar.Size = new System.Drawing.Size(135, 22);
            this.txtEliminar.TabIndex = 6;
            // 
            // txtBuscar
            // 
            this.txtBuscar.Location = new System.Drawing.Point(196, 352);
            this.txtBuscar.Name = "txtBuscar";
            this.txtBuscar.Size = new System.Drawing.Size(135, 22);
            this.txtBuscar.TabIndex = 7;
            // 
            // btnPre
            // 
            this.btnPre.Location = new System.Drawing.Point(1333, 204);
            this.btnPre.Name = "btnPre";
            this.btnPre.Size = new System.Drawing.Size(173, 40);
            this.btnPre.TabIndex = 8;
            this.btnPre.Text = "Pre-Orden";
            this.btnPre.UseVisualStyleBackColor = true;
            this.btnPre.Click += new System.EventHandler(this.button1_Click);
            // 
            // btnPost
            // 
            this.btnPost.Location = new System.Drawing.Point(1333, 297);
            this.btnPost.Name = "btnPost";
            this.btnPost.Size = new System.Drawing.Size(173, 41);
            this.btnPost.TabIndex = 9;
            this.btnPost.Text = "Post-Orden";
            this.btnPost.UseVisualStyleBackColor = true;
            this.btnPost.Click += new System.EventHandler(this.btnPost_Click);
            // 
            // btnEn
            // 
            this.btnEn.Location = new System.Drawing.Point(1333, 392);
            this.btnEn.Name = "btnEn";
            this.btnEn.Size = new System.Drawing.Size(173, 40);
            this.btnEn.TabIndex = 10;
            this.btnEn.Text = "En-Orden";
            this.btnEn.UseVisualStyleBackColor = true;
            this.btnEn.Click += new System.EventHandler(this.btnEn_Click);
            // 
            // lblRecorrido
            // 
            this.lblRecorrido.AutoSize = true;
            this.lblRecorrido.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.lblRecorrido.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblRecorrido.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.lblRecorrido.Location = new System.Drawing.Point(695, 552);
            this.lblRecorrido.Margin = new System.Windows.Forms.Padding(3, 4, 3, 0);
            this.lblRecorrido.MaximumSize = new System.Drawing.Size(500, 500);
            this.lblRecorrido.MinimumSize = new System.Drawing.Size(300, 20);
            this.lblRecorrido.Name = "lblRecorrido";
            this.lblRecorrido.Size = new System.Drawing.Size(300, 20);
            this.lblRecorrido.TabIndex = 12;
            this.lblRecorrido.Text = "Recorrido: ";
            this.lblRecorrido.Click += new System.EventHandler(this.lblRecorrido_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(1347, 150);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(142, 29);
            this.label2.TabIndex = 13;
            this.label2.Text = "Recorridos";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.lblCantidad);
            this.groupBox1.Controls.Add(this.lblSuma);
            this.groupBox1.Controls.Add(this.lblAltura);
            this.groupBox1.Controls.Add(this.btnCantidad);
            this.groupBox1.Controls.Add(this.btnSuma);
            this.groupBox1.Controls.Add(this.btnAltura);
            this.groupBox1.Location = new System.Drawing.Point(13, 427);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(348, 182);
            this.groupBox1.TabIndex = 14;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Operaciones";
            // 
            // lblCantidad
            // 
            this.lblCantidad.AutoSize = true;
            this.lblCantidad.Location = new System.Drawing.Point(239, 132);
            this.lblCantidad.Name = "lblCantidad";
            this.lblCantidad.Size = new System.Drawing.Size(14, 16);
            this.lblCantidad.TabIndex = 5;
            this.lblCantidad.Text = "0";
            // 
            // lblSuma
            // 
            this.lblSuma.AutoSize = true;
            this.lblSuma.Location = new System.Drawing.Point(239, 86);
            this.lblSuma.Name = "lblSuma";
            this.lblSuma.Size = new System.Drawing.Size(14, 16);
            this.lblSuma.TabIndex = 4;
            this.lblSuma.Text = "0";
            // 
            // lblAltura
            // 
            this.lblAltura.AutoSize = true;
            this.lblAltura.Location = new System.Drawing.Point(239, 36);
            this.lblAltura.Name = "lblAltura";
            this.lblAltura.Size = new System.Drawing.Size(14, 16);
            this.lblAltura.TabIndex = 3;
            this.lblAltura.Text = "0";
            // 
            // btnCantidad
            // 
            this.btnCantidad.Location = new System.Drawing.Point(16, 125);
            this.btnCantidad.Name = "btnCantidad";
            this.btnCantidad.Size = new System.Drawing.Size(161, 23);
            this.btnCantidad.TabIndex = 2;
            this.btnCantidad.Text = "Cantidad de nodos";
            this.btnCantidad.UseVisualStyleBackColor = true;
            this.btnCantidad.Click += new System.EventHandler(this.btnCantidad_Click);
            // 
            // btnSuma
            // 
            this.btnSuma.Location = new System.Drawing.Point(16, 79);
            this.btnSuma.Name = "btnSuma";
            this.btnSuma.Size = new System.Drawing.Size(161, 23);
            this.btnSuma.TabIndex = 1;
            this.btnSuma.Text = "Suma de los nodos";
            this.btnSuma.UseVisualStyleBackColor = true;
            this.btnSuma.Click += new System.EventHandler(this.btnSuma_Click);
            // 
            // btnAltura
            // 
            this.btnAltura.Location = new System.Drawing.Point(16, 33);
            this.btnAltura.Name = "btnAltura";
            this.btnAltura.Size = new System.Drawing.Size(161, 23);
            this.btnAltura.TabIndex = 0;
            this.btnAltura.Text = "Determinar Altura";
            this.btnAltura.UseVisualStyleBackColor = true;
            this.btnAltura.Click += new System.EventHandler(this.btnAltura_Click);
            // 
            // btnCargar
            // 
            this.btnCargar.Location = new System.Drawing.Point(13, 18);
            this.btnCargar.Name = "btnCargar";
            this.btnCargar.Size = new System.Drawing.Size(177, 35);
            this.btnCargar.TabIndex = 15;
            this.btnCargar.Text = "Importar";
            this.btnCargar.UseVisualStyleBackColor = true;
            this.btnCargar.Click += new System.EventHandler(this.btnCargar_Click);
            // 
            // btnGuardar
            // 
            this.btnGuardar.Location = new System.Drawing.Point(214, 18);
            this.btnGuardar.Name = "btnGuardar";
            this.btnGuardar.Size = new System.Drawing.Size(177, 35);
            this.btnGuardar.TabIndex = 16;
            this.btnGuardar.Text = "Exportar";
            this.btnGuardar.UseVisualStyleBackColor = true;
            this.btnGuardar.Click += new System.EventHandler(this.btnGuardar_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1549, 621);
            this.Controls.Add(this.btnGuardar);
            this.Controls.Add(this.btnCargar);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.btnEn);
            this.Controls.Add(this.lblRecorrido);
            this.Controls.Add(this.btnPost);
            this.Controls.Add(this.btnPre);
            this.Controls.Add(this.txtBuscar);
            this.Controls.Add(this.txtEliminar);
            this.Controls.Add(this.txtDato);
            this.Controls.Add(this.btnBuscar);
            this.Controls.Add(this.btnEliminar);
            this.Controls.Add(this.btnInsertar);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button btnInsertar;
        private System.Windows.Forms.Button btnEliminar;
        private System.Windows.Forms.Button btnBuscar;
        private System.Windows.Forms.TextBox txtDato;
        private System.Windows.Forms.TextBox txtEliminar;
        private System.Windows.Forms.TextBox txtBuscar;
        private System.Windows.Forms.Button btnPre;
        private System.Windows.Forms.Button btnPost;
        private System.Windows.Forms.Button btnEn;
        private System.Windows.Forms.Label lblRecorrido;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label lblCantidad;
        private System.Windows.Forms.Label lblSuma;
        private System.Windows.Forms.Label lblAltura;
        private System.Windows.Forms.Button btnCantidad;
        private System.Windows.Forms.Button btnSuma;
        private System.Windows.Forms.Button btnAltura;
        private System.Windows.Forms.Button btnCargar;
        private System.Windows.Forms.Button btnGuardar;
    }
}

