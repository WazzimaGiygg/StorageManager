import psutil

def listar_processos():
    print(f"{'PID':<10} {'Nome':<25} {'Uso de CPU (%)':<15} {'Uso de Memória (MB)':<20}")
    print("=" * 70)
    
    for processo in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            pid = processo.info['pid']
            nome = processo.info['name']
            cpu = processo.info['cpu_percent']
            memoria = processo.info['memory_info'].rss / (1024 * 1024)  # Converte para MB
            
            print(f"{pid:<10} {nome:<25} {cpu:<15} {memoria:<20.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

if __name__ == "__main__":
    listar_processos()
