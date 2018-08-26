using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Storage_Manager
{
    public partial class Login : Form
    {
        public Login()
        {
            InitializeComponent();
            try
            {
               
                string[] lines = File.ReadAllLines(@"administrator.nukephoenix");
            }
            catch (Exception)
            {
                this.Hide();
                groupBox1.Enabled = false;
                MessageBox.Show("The Account Administrator dont exist! To Progress you need create!");
                adminkey obj = new adminkey();
                obj.Show();
                this.Hide();

            }
            

        }
        string storagesgbd,concrete;
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                string user = textBox1.Text;
                string keys = textBox2.Text;
                string[] lines = File.ReadAllLines(@"" + storagesgbd + textBox1.Text + ".nukephoenix");
                concrete = (@"" + storagesgbd + textBox1.Text + ".txt".ToString());
                listBox1.Items.Add(textBox1.Text);
                if (lines[0] == keys)
                {
                    File.WriteAllLines(@"configure.nukephoenix", listBox1.Items.OfType<string>());
                    Desktop.Desktop obj = new Desktop.Desktop();
                    obj.Show();
                    this.Hide();

                }
                else
                {
                    MessageBox.Show("Invalid Key!");
                }
            }
            catch (Exception)
            {

                MessageBox.Show (string.Format ("Invalid Account (ERROR LOGIN) ", concrete, "Error", MessageBoxButtons.OK));
            }
           
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void eventLog1_EntryWritten(object sender, System.Diagnostics.EntryWrittenEventArgs e)
        {

        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }
    }
}
