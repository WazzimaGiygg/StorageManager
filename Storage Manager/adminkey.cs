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
    public partial class adminkey : Form
    {
        public adminkey()
        {
            InitializeComponent();
        }
        
        private void adminkey_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox2.Text = textBox2.Text + button2.Text;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            textBox2.Text = textBox2.Text + button11.Text;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            textBox2.Text = textBox2.Text + button8.Text;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            textBox2.Text = textBox2.Text + button9.Text;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            textBox2.Text = textBox2.Text + button10.Text;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            textBox2.Text = textBox2.Text + button7.Text;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            textBox2.Text = textBox2.Text + button6.Text;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            textBox2.Text = textBox2.Text + button5.Text;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            textBox2.Text = textBox2.Text + button4.Text;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            textBox2.Text = textBox2.Text + button3.Text;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Add(listBox1.Text + textBox1.Text);
            listBox1.Items.Add(listBox1.Text + textBox2.Text);
            string key = textBox1.Text;
            string subkey = textBox2.Text;
            if (textBox1.Text == textBox3.Text && textBox2.Text == textBox4.Text )
            {
                File.WriteAllLines(@"administrator.nukephoenix", listBox1.Items.OfType<string>());
                MessageBox.Show("Account created!");
                System.Windows.Forms.Application.Exit();
            }
            else if (textBox1.Text == textBox4.Text && textBox2.Text == textBox3.Text)
            {
                MessageBox.Show("Wrong field texts are writed!");
            }
            else
            {
                MessageBox.Show("The keys dont match!");
            }
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void adminkey_FormClosed(object sender, FormClosedEventArgs e)
        {
            System.Windows.Forms.Application.Exit();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            textBox4.Text = textBox4.Text + button12.Text;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            textBox4.Text = textBox4.Text + button13.Text;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            textBox4.Text = textBox4.Text + button14.Text;
        }

        private void button15_Click(object sender, EventArgs e)
        {
            textBox4.Text = textBox4.Text + button15.Text;
        }

        private void button16_Click(object sender, EventArgs e)
        {
            textBox4.Text = textBox4.Text + button16.Text;
        }

        private void button17_Click(object sender, EventArgs e)
        {
            textBox4.Text = textBox4.Text + button17.Text;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            textBox4.Text = textBox4.Text + button18.Text;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            textBox4.Text = textBox4.Text + button19.Text;
        }

        private void button20_Click(object sender, EventArgs e)
        {
            textBox4.Text = textBox4.Text + button20.Text;
        }

        private void button21_Click(object sender, EventArgs e)
        {
            textBox4.Text = textBox4.Text + button21.Text;
        }
    }
}
