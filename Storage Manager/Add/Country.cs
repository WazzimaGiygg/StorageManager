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
    public partial class Country : Form
    {
        public Country()
        {
            InitializeComponent();

        }
        string economic;
        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void Country_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int count = 1;
            bool veridico = false;
            label4.Text = count.ToString();
            while (veridico == false)
                
            {
                try
                {
                    
                    string[] lines = File.ReadAllLines(@"country" + label4.Text + ".txt");
                    count = count + 1;
                    label4.Text = count.ToString();
                   /* MessageBox.Show("test1");*/

                }
                catch (Exception)
                {
                    label3.Text = economic.ToString();
                    listBox1.Items.Add(listBox1.Text + comboBox1.Text);
                    listBox1.Items.Add(listBox1.Text + comboBox2.Text);
                    listBox1.Items.Add(listBox1.Text + label3.Text);

                    label4.Text = count.ToString();
                    File.WriteAllLines(@"country" + label4.Text + ".txt", listBox1.Items.OfType<string>());
                    veridico = true;
                    this.Close();
                    /*MessageBox.Show("test2");*/
                }

            }
           
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            economic = radioButton1.Text;
            label3.Text = economic.ToString();
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            economic = radioButton2.Text;
            label3.Text = economic.ToString();
        }

        private void radioButton4_CheckedChanged(object sender, EventArgs e)
        {
            economic = radioButton4.Text;
            label3.Text = economic.ToString();
        }

        private void radioButton7_CheckedChanged(object sender, EventArgs e)
        {
            economic = radioButton7.Text;
            label3.Text = economic.ToString();
        }

        private void radioButton8_CheckedChanged(object sender, EventArgs e)
        {
            economic = radioButton8.Text;
            label3.Text = economic.ToString();
        }

        private void radioButton5_CheckedChanged(object sender, EventArgs e)
        {
            economic = radioButton5.Text;
            label3.Text = economic.ToString();
        }

        private void radioButton10_CheckedChanged(object sender, EventArgs e)
        {
            economic = radioButton10.Text;
            label3.Text = economic.ToString();
        }

        private void radioButton11_CheckedChanged(object sender, EventArgs e)
        {
            economic = radioButton11.Text;
            label3.Text = economic.ToString();
        }

        private void radioButton12_CheckedChanged(object sender, EventArgs e)
        {
            economic = radioButton12.Text;
            label3.Text = economic.ToString();
        }

        private void radioButton9_CheckedChanged(object sender, EventArgs e)
        {
            economic = radioButton9.Text;
            label3.Text = economic.ToString();
        }

        private void radioButton6_CheckedChanged(object sender, EventArgs e)
        {
            economic = radioButton6.Text;
            label3.Text = economic.ToString();
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            economic = radioButton3.Text;
            label3.Text = economic.ToString();
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            economic = "Now Valid";
            label3.Text = economic.ToString();
            groupBox2.Enabled = false;
            
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void groupBox2_Enter(object sender, EventArgs e)
        {

        }

        private void groupBox3_Enter(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }
    }
}
