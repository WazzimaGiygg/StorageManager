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
    public partial class Company : Form
    {
        public Company()
        {
            InitializeComponent();
        }

        private void Company_Load(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

            bool ahva = false;
            int cont = 1;
            while (ahva == false)
            {

                try
                {
                    label6.Text = cont.ToString();
                    string[] lines = File.ReadAllLines(@"companyreg" + label6.Text + ".txt");
                    cont = cont + 1;


                }
                catch (Exception)
                {
                    listBox1.Items.Add(listBox1.Text + textBox1.Text);
                    listBox1.Items.Add(listBox1.Text + textBox2.Text);
                    listBox1.Items.Add(listBox1.Text + textBox3.Text);
                    listBox1.Items.Add(listBox1.Text + textBox4.Text);
                    listBox1.Items.Add(listBox1.Text + textBox5.Text);
                    listBox1.Items.Add(listBox1.Text + pictureBox1.ImageLocation);
                    File.WriteAllLines(@"companyreg" + label6.Text + ".txt", listBox1.Items.OfType<string>());
                    ahva = true;
                    this.Close();
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            try
            {
                string[] lines = File.ReadAllLines(@"companyreg" + textBox6.Text + ".txt");
                textBox1.Text = lines[0];
                textBox2.Text = lines[1];
                textBox3.Text = lines[2];
                textBox4.Text = lines[3];
                textBox5.Text = lines[4];
                pictureBox1.ImageLocation = lines[5];
            }
            catch (Exception)
            {

                MessageBox.Show("This Register are not valid");
            }
            
        }

        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                listBox1.Items.Add(listBox1.Text + textBox1.Text);
                listBox1.Items.Add(listBox1.Text + textBox2.Text);
                listBox1.Items.Add(listBox1.Text + textBox3.Text);
                listBox1.Items.Add(listBox1.Text + textBox4.Text);
                listBox1.Items.Add(listBox1.Text + textBox5.Text);
                listBox1.Items.Add(listBox1.Text + pictureBox1.ImageLocation);
                File.WriteAllLines(@"companyreg" + label6.Text + ".txt", listBox1.Items.OfType<string>());
            }
            catch (Exception)
            {

                MessageBox.Show("Unknown error");

            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK) ;
            {
                pictureBox1.ImageLocation = openFileDialog1.FileName;
            }

        }
    }
}
