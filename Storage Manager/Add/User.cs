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
    public partial class User : Form
    {
        public User()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
           

           
        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            bool ahva = false;
            int cont = 1;
            while (ahva == false)
            {

                try
                {
                    label4.Text = cont.ToString();
                    string[] lines = File.ReadAllLines(@"user" + label4.Text + ".txt");
                    cont = cont + 1;


                }
                catch (Exception)
                {


                    listBox1.Items.Add(listBox1.Text + textBox1.Text);
                    listBox1.Items.Add(listBox1.Text + textBox2.Text);
                    listBox1.Items.Add(listBox1.Text + textBox3.Text);
                    listBox1.Items.Add(listBox1.Text + textBox4.Text);
                    if (textBox1.Text == textBox6.Text && textBox2.Text == textBox5.Text)
                    {
                        File.WriteAllLines(@"user" + label4.Text + ".nukephoenix", listBox1.Items.OfType<string>());
                        MessageBox.Show("Account created!");
                        groupBox1.Enabled = false;
                    }
                    else if (textBox1.Text == textBox5.Text && textBox2.Text == textBox6.Text)
                    {
                        MessageBox.Show("Wrong field texts are writed!");
                        this.Close();
                    }
                    else
                    {
                        MessageBox.Show("The keys dont match!");
                        this.Close();
                    }
                    ahva = true;
                    
                }
            }
        }
    }
}
