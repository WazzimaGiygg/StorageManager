using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing.Printing;
using System.IO;

namespace Storage_Manager.Desktop
{
    public partial class Desktop : Form
    {
        public Desktop()
        {
            InitializeComponent();
            string[] lines = File.ReadAllLines(@"configure.nukephoenix");
            string adm = lines[0].ToString();
            if (adm == "administrator")
            {

            }
            else
            {

                userToolStripMenuItem.Visible = false;
                systemConfigurationToolStripMenuItem.Visible = false;
            }
        }
        bool a,b,c,d,e,f,g,h,i,j = false;
        private void toolStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void copyToolStripButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Beta version!");
        }

        private void newToolStripButton_Click(object sender, EventArgs e)
        {
            Saller.Saller frm = new Saller.Saller();
            frm.TopLevel = false;
            frm.AutoScroll = true;

            panel1.Controls.Add(frm);
            frm.Show();
        }

        private void openToolStripButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Beta version!");
        }

        private void saveToolStripButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Beta version!");
        }

        private void printToolStripButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Beta version!");
        }

        private void toolStripSeparator_Click(object sender, EventArgs e)
        {

        }

        private void cutToolStripButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Beta version!");
        }

        private void pasteToolStripButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Beta version!");
        }

        private void toolStripSeparator1_Click(object sender, EventArgs e)
        {

        }

        private void helpToolStripButton_Click(object sender, EventArgs e)
        {

        }

        private void Desktop_Load(object sender, EventArgs e)
        {

        }

        private void newClientToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (a == true)
            {
                Add.Client frm = new Add.Client();
                frm.TopLevel = false;
                frm.AutoScroll = true;

                panel1.Controls.Add(frm);
                frm.Show();
                a = true;
            }
            else
            {
                Add.Client frm = new Add.Client();
                frm.TopLevel = false;
                frm.AutoScroll = true;

                panel1.Controls.Add(frm);
                frm.Show();
                a = true;
            }
        }

        private void newProductToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void newCompanyToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Add.Company frm = new Add.Company();
            frm.TopLevel = false;
            frm.AutoScroll = true;

            panel1.Controls.Add(frm);
            frm.Show();
        }

        private void Desktop_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Space && e.Control)
            {
                BackColor = Color.Orange;
            }
            else if (e.KeyCode == Keys.Space)
            {
                BackColor = Color.Red;
            }
            else if (e.KeyCode == Keys.Return)
            {
                Add.Client frm = new Add.Client();
                frm.TopLevel = false;
                frm.AutoScroll = true;

                panel1.Controls.Add(frm);
                frm.Show();
            }
            else if (e.KeyCode == Keys.Enter && e.Alt && e.Control)
            {
                Add.Client frm = new Add.Client();
                frm.TopLevel = false;
                frm.AutoScroll = true;

                panel1.Controls.Add(frm);
                frm.Show();
            }
        }

        private void newCompanyToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            Add.Company frm = new Add.Company();
            frm.TopLevel = false;
            frm.AutoScroll = true;

            panel1.Controls.Add(frm);
            frm.Show();
        }

        private void newClientToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            Add.Client frm = new Add.Client();
            frm.TopLevel = false;
            frm.AutoScroll = true;

            panel1.Controls.Add(frm);
            frm.Show();
        }

        private void Desktop_KeyUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Space || e.KeyCode == Keys.Return)
            {
                BackColor = SystemColors.Control;
            }


        }

        private void Desktop_FormClosing(object sender, FormClosingEventArgs e)
        {
            System.Windows.Forms.Application.Exit();
          

        }

        private void Desktop_MouseEnter(object sender, EventArgs e)
        {
            toolStrip1.BackColor = Color.Black;
        }

        private void newCountryToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Add.Country frm = new Add.Country();
            frm.TopLevel = false;
            frm.AutoScroll = true;

            panel1.Controls.Add(frm);
            frm.Show();
        }

        private void newProductToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            Add.Product frm = new Add.Product();
            frm.TopLevel = false;
            frm.AutoScroll = true;

            panel1.Controls.Add(frm);
            frm.Show();
        }

        private void newToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Saller.Saller frm = new Saller.Saller();
            frm.TopLevel = false;
            frm.AutoScroll = true;

            panel1.Controls.Add(frm);
            frm.Show();
        }

        private void editViewToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Saller.Sellreg frm = new Saller.Sellreg();
            frm.TopLevel = false;
            frm.AutoScroll = true;

            panel1.Controls.Add(frm);
            frm.Show();
        }

        private void printDocument1_PrintPage(object sender, PrintPageEventArgs e)
        {
            Panel grd = new Panel();
            Bitmap bmp = new Bitmap(grd.Width, grd.Height, grd.CreateGraphics());
            grd.DrawToBitmap(bmp, new Rectangle(0, 0, grd.Width, grd.Height));
            RectangleF bounds = e.PageSettings.PrintableArea;
            float factor = ((float)bmp.Height / (float)bmp.Width);
            e.Graphics.DrawImage(bmp, bounds.Left, bounds.Top, bounds.Width, factor * bounds.Width);
        }

        private void userToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Add.User frm = new Add.User();
            frm.TopLevel = false;
            frm.AutoScroll = true;

            panel1.Controls.Add(frm);
            frm.Show();
        }

        private void systemConfigurationToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Beta version!");
        }

        private void aboutManagerStorageToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Help.help frm = new Help.help();
            frm.TopLevel = false;
            frm.AutoScroll = true;

            panel1.Controls.Add(frm);
            frm.Show();
        }

        private void helpTopicsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Beta version!");
        }

        private void changePasswordToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Beta version!");
        }

        private void toolStripButton1_Click(object sender, EventArgs e)
        {

        }

        private void Desktop_MouseLeave(object sender, EventArgs e)
        {
            toolStrip1.BackColor = SystemColors.Control;
        }

        private void toolStrip1_MouseEnter(object sender, EventArgs e)
        {
            toolStrip1.BackColor = Color.Red;
        }

        private void toolStrip1_MouseLeave(object sender, EventArgs e)
        {
            toolStrip1.BackColor = SystemColors.Control;
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            System.Windows.Forms.Application.Exit();

        }

        private void toolStripButton1_MouseEnter(object sender, EventArgs e)
        {
            
        }

        private void Desktop_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == '6') e.Handled = true;
        }

        private void toolStripTextBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == '6') e.Handled = true;
        }

        private void toolStripTextBox1_Click(object sender, EventArgs e)
        {

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }
    }
}

