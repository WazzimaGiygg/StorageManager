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
    public partial class Client : Form
    {
        public Client()
        {
            InitializeComponent();
            
            
            {
               

            }
           
        }
        string diretorio;
        private void Client_Load(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void comboBox4_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void groupBox2_Enter(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            bool ahva = false;
            int cont = 1;
            while(ahva == false)
            {
                
                try
                {
                    label15.Text = cont.ToString();
                    string[] lines = File.ReadAllLines(@"clientreg" + label15.Text + ".txt");
                    cont = cont + 1;


                }
                catch (Exception)
                {


                    listBox1.Items.Add(listBox1.Text + comboBox1.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox2.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox3.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox4.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox5.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox6.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox7.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox8.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox9.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox10.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox11.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox12.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox13.Text);
                    listBox1.Items.Add(listBox1.Text + textBox1.Text);
                    listBox1.Items.Add(listBox1.Text + textBox2.Text);
                    listBox1.Items.Add(listBox1.Text + textBox3.Text);

                    File.WriteAllLines(@"clientreg" + label15.Text + ".txt", listBox1.Items.OfType<string>());
                    ahva = true;
                    this.Close();
                }
            }
            
        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void comboBox3_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void comboBox5_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void comboBox6_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void comboBox7_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void comboBox8_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void groupBox3_Enter(object sender, EventArgs e)
        {

        }

        private void comboBox9_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label8_Click(object sender, EventArgs e)
        {

        }

        private void comboBox10_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void comboBox11_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label10_Click(object sender, EventArgs e)
        {

        }

        private void comboBox12_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label11_Click(object sender, EventArgs e)
        {

        }

        private void groupBox4_Enter(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label12_Click(object sender, EventArgs e)
        {

        }

        private void label13_Click(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void label14_Click(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label15_Click(object sender, EventArgs e)
        {
        
        }

        private void label16_Click(object sender, EventArgs e)
        {

        }

        private void comboBox13_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

            try
            {
                string[] lines = File.ReadAllLines(@"clientreg" + textBox4.Text + ".txt");
                listBox2.Items.AddRange(lines);
                comboBox1.Text = lines[0];
                comboBox2.Text = lines[1];
                comboBox3.Text = lines[2];
                comboBox4.Text = lines[3];
                comboBox5.Text = lines[4];
                comboBox6.Text = lines[5];
                comboBox7.Text = lines[6];
                comboBox8.Text = lines[7];
                comboBox9.Text = lines[8];
                comboBox10.Text = lines[9];
                comboBox11.Text = lines[10];
                comboBox12.Text = lines[11];
                textBox1.Text = lines[13];
                textBox2.Text = lines[14];
                textBox3.Text = lines[15];
                comboBox13.Text = lines[12];
            }
            catch (Exception)
            {

                MessageBox.Show("This Register are not valid");
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {


            listBox1.Items.Add(listBox1.Text + comboBox1.Text);
            listBox1.Items.Add(listBox1.Text + comboBox2.Text);
            listBox1.Items.Add(listBox1.Text + comboBox3.Text);
            listBox1.Items.Add(listBox1.Text + comboBox4.Text);
            listBox1.Items.Add(listBox1.Text + comboBox5.Text);
            listBox1.Items.Add(listBox1.Text + comboBox6.Text);
            listBox1.Items.Add(listBox1.Text + comboBox7.Text);
            listBox1.Items.Add(listBox1.Text + comboBox8.Text);
            listBox1.Items.Add(listBox1.Text + comboBox9.Text);
            listBox1.Items.Add(listBox1.Text + comboBox10.Text);
            listBox1.Items.Add(listBox1.Text + comboBox11.Text);
            listBox1.Items.Add(listBox1.Text + comboBox12.Text);
            listBox1.Items.Add(listBox1.Text + comboBox13.Text);
            listBox1.Items.Add(listBox1.Text + textBox1.Text);
            listBox1.Items.Add(listBox1.Text + textBox2.Text);
            listBox1.Items.Add(listBox1.Text + textBox3.Text);

            File.WriteAllLines(@"clientreg" + textBox4.Text + ".txt", listBox1.Items.OfType<string>());
            
        }

        private void button4_Click(object sender, EventArgs e)
        {
            comboBox1.Text = "";
            comboBox2.Text = "";
            comboBox3.Text = "";
            comboBox4.Text = "";
            comboBox5.Text = "";
            comboBox6.Text = "";
            comboBox7.Text = "";
            comboBox8.Text = "";
            comboBox9.Text = "";
            comboBox10.Text = "";
            comboBox11.Text = "";
            comboBox12.Text = "";
            comboBox13.Text = "";
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";

        }

        private void Client_FormClosing(object sender, FormClosingEventArgs e)
        {
            
            
        }

        private void Client_FormClosed(object sender, FormClosedEventArgs e)
        {

        }

        private void label17_Click(object sender, EventArgs e)
        {

        }

        private void listBox3_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
