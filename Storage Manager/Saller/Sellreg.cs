using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Printing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Storage_Manager.Saller
{
    public partial class Sellreg : Form
    {
        public Sellreg()
        {
            InitializeComponent();
            label1.Visible = false;
            label2.Visible = false;
            label3.Visible = false;
            label4.Visible = false;
            label5.Visible = false;
            label6.Visible = false;
            label7.Visible = false;
            label8.Visible = false;
            label9.Visible = false;
            label10.Visible = false;
            label11.Visible = false;
            label12.Visible = false;
            label13.Visible = false;
        }

        private void toolStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void toolStripButton2_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void toolStripButton1_Click(object sender, EventArgs e)
        {
            try
            {
                string[] lines = File.ReadAllLines(@"sellreg" + toolStripTextBox1.Text + ".txt");
                label7.Text = lines[0];
                label8.Text = lines[1];
                label9.Text = lines[2];
                label10.Text = lines[4] + " | " + lines[5] + " | " + lines[6] + " | " + lines[7];
                label11.Text = lines[7];
                label13.Text = lines[3];
                label1.Visible = true;
                label2.Visible = true;
                label3.Visible = true;
                label4.Visible = true;
                label5.Visible = true;
                label6.Visible = true;
                label7.Visible = true;
                label8.Visible = true;
                label9.Visible = true;
                label10.Visible = true;
                label11.Visible = true;
                label12.Visible = true;
                label13.Visible = true;
            }
            catch (Exception)
            {

                MessageBox.Show("This register dont has valid!");
            }
        }

        private void toolStripTextBox1_Click(object sender, EventArgs e)
        {

        }

        private void printDocument1_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            Panel grd = new Panel();
            Bitmap bmp = new Bitmap(grd.Width, grd.Height, grd.CreateGraphics());
            grd.DrawToBitmap(bmp, new Rectangle(0, 0, grd.Width, grd.Height));
            RectangleF bounds = e.PageSettings.PrintableArea;
            float factor = ((float)bmp.Height / (float)bmp.Width);
            e.Graphics.DrawImage(bmp, bounds.Left, bounds.Top, bounds.Width, factor * bounds.Width);
        }

        private void Sellreg_Load(object sender, EventArgs e)
        {

        }

        private void imprimirToolStripButton_Click(object sender, EventArgs e)
        {
            PrintDialog myPrintDialog = new PrintDialog();
            System.Drawing.Bitmap memoryImage = new System.Drawing.Bitmap(panel1.Width, panel1.Height);
            panel1.DrawToBitmap(memoryImage, panel1.ClientRectangle);
            if (myPrintDialog.ShowDialog() == DialogResult.OK)
            {
                System.Drawing.Printing.PrinterSettings values;
                values = myPrintDialog.PrinterSettings;
                myPrintDialog.Document = printDocument1;
                printDocument1.PrintController = new StandardPrintController();
                printDocument1.Print();
            }
            printDocument1.Dispose();
        }
    }
}
