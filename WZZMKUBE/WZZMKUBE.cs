using System;
using System.Diagnostics;
using System.Threading;
using System.Windows.Forms;

namespace Launcher
{
    static class Program
    {
        [STAThread]
        static void Main()
        {
            bool isAnotherInstance;
            using (Mutex mutex = new Mutex(true, "UniqueAppMutexName", out isAnotherInstance))
            {
                if (isAnotherInstance)
                {
                    // Executa o aplicativo original
                    Process.Start("../abrir.exe");
                }
                else
                {
                    MessageBox.Show("Outra instância do aplicativo já está em execução.");
                }
            }
        }
    }
}
