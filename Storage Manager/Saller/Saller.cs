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

namespace Storage_Manager.Saller
{
    public partial class Saller : Form
    {
        public Saller()
        {
            InitializeComponent();
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void groupBox3_Enter(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                string[] lines = File.ReadAllLines(@"clientreg" + textBox1.Text + ".txt");
                label4.Text = lines[0];
                label6.Text = (lines[6] + " | " + lines[7] + " | " + lines[8] + " | " + lines[9]);
                label8.Text = (lines[3] + " | " + lines[4]);
            }
            catch (Exception)
            {

                MessageBox.Show("This register dont has valid!");
            }
            
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void groupBox2_Enter(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

            try
            {
                string[] linev = File.ReadAllLines(@"productreg" + textBox2.Text + ".txt");
                label10.Text = linev[0];
                label15.Text = linev[2];
            }
            catch (Exception)
            {

                MessageBox.Show("This register dont has valid!");
            }
           
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        private void label8_Click(object sender, EventArgs e)
        {

        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void label10_Click(object sender, EventArgs e)
        {

        }

        private void label11_Click(object sender, EventArgs e)
        {

        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void label12_Click(object sender, EventArgs e)
        {

        }

        private void label13_Click(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            double v1 = Double.Parse(label15.Text);
            double v2 = Double.Parse(textBox3.Text);
            double resultado = 0;
            resultado = v1 / v2;
            label18.Text = v2.ToString() + "X" + resultado.ToString();
        }

        private void label14_Click(object sender, EventArgs e)
        {

        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            bool ahva = false;
            int cont = 1;
            while (ahva == false)
            {

                try
                {
                    label17.Text = cont.ToString();
                    string[] lines = File.ReadAllLines(@"sellreg" + label17.Text + ".txt");
                    cont = cont + 1;


                }
                catch (Exception)
                {


                    listBox1.Items.Add(listBox1.Text + label4.Text);
                    listBox1.Items.Add(listBox1.Text + label6.Text);
                    listBox1.Items.Add(listBox1.Text + label8.Text);
                    listBox1.Items.Add(listBox1.Text + label10.Text);
                    listBox1.Items.Add(listBox1.Text + label15.Text);
                    listBox1.Items.Add(listBox1.Text + textBox3.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox1.Text);
                    listBox1.Items.Add(listBox1.Text + dateTimePicker1.Text);

                    File.WriteAllLines(@"sellreg" + label17.Text + ".txt", listBox1.Items.OfType<string>());
                    ahva = true;
                    this.Close();
                }
            }
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void comboBox1_Enter(object sender, EventArgs e)
        {
            
        }

        private void label15_Click(object sender, EventArgs e)
        {
            double v1 = Double.Parse(label15.Text);
            double v2 = Double.Parse(textBox3.Text);
            double resultado = 0;
            resultado = v1 / v2;
            label18.Text = v2.ToString() + "X" +  resultado.ToString();

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void label18_Click(object sender, EventArgs e)
        {

        }
    }
}
