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

namespace Storage_Manager.Add
{
    public partial class Product : Form
    {
        public Product()
        {

            InitializeComponent();
            bool nox = false;
            while (nox == true)
            {
                int cont = 1;
                label11.Text = cont.ToString();
                try
                {
                    string[] linesx = File.ReadAllLines(@"companyreg" + label11.Text + ".txt");
                    listBox3.Items.Add(linesx[0]);
                    listBox6.Items.Add(linesx[0]);
                    cont = cont + 1;
                }
                catch (Exception)
                {
                    nox = true;

                }
            }
            
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                bool ahva = false;
                int cont = 1;
                string company = listBox3.SelectedItem.ToString();
                while (ahva == false)
                {
                    try
                    {
                        try
                        {
                            label6.Text = cont.ToString();
                            string[] lines = File.ReadAllLines(@"productreg" + label6.Text + ".txt");
                            cont = cont + 1;


                        }
                        catch (Exception)
                        {
                            label14.Text = company.ToString();
                            listBox1.Items.Add(listBox1.Text + textBox1.Text);
                            listBox1.Items.Add(listBox1.Text + textBox2.Text);
                            listBox1.Items.Add(listBox1.Text + textBox3.Text);
                            listBox1.Items.Add(listBox1.Text + textBox4.Text);
                            listBox1.Items.Add(listBox1.Text + label14.Text);
                            File.WriteAllLines(@"productreg" + label6.Text + ".txt", listBox1.Items.OfType<string>());
                            ahva = true;
                            this.Close();
                        }
                    }
                    catch (Exception)
                    {

                        MessageBox.Show("Register dont follow the requesits.");
                    }


                }
            }
            catch (Exception)
            {

                MessageBox.Show("This Register are not valid");
            }
            
        }

        private void tabPage1_Click(object sender, EventArgs e)
        {

        }

        private void listBox3_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                string company = listBox6.SelectedItem.ToString();
                label14.Text = company.ToString();
                listBox1.Items.Add(listBox1.Text + textBox8.Text);
                listBox1.Items.Add(listBox1.Text + textBox7.Text);
                listBox1.Items.Add(listBox1.Text + textBox6.Text);
                listBox1.Items.Add(listBox1.Text + textBox5.Text);
                listBox1.Items.Add(listBox1.Text + label14.Text);
                File.WriteAllLines(@"productreg" + textBox9.Text + ".txt", listBox1.Items.OfType<string>());
                this.Close();
            }
            catch (Exception)
            {

                MessageBox.Show("This Register are not valid");
            }
           


        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {

        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox7_TextChanged(object sender, EventArgs e)
        {

        }

        private void label8_Click(object sender, EventArgs e)
        {

        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void textBox8_TextChanged(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

            try
            {
                string[] lines = File.ReadAllLines(@"productreg" + textBox9.Text + ".txt");
                textBox8.Text = lines[0];
                textBox7.Text = lines[1];
                textBox6.Text = lines[2];
                textBox5.Text = lines[3];
                label13.Text = lines[4];
            }
            catch (Exception)
            {

                MessageBox.Show("This Register are not valid");
            }

        }
    }
}
