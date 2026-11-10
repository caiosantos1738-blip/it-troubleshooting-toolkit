
# IT Troubleshooting Toolkit

A Python-based diagnostic toolkit designed to support IT troubleshooting, system analysis, and technical support operations.

The project provides command-line tools to diagnose network connectivity and Linux system resources, generate technical reports, and produce automatic recommendations based on diagnostic results.

## Features

### Network Diagnostics
- ICMP connectivity testing using ping.
- DNS resolution checks.
- Default gateway detection.
- TCP port connectivity testing.

### Linux System Diagnostics
- CPU model, logical cores, and load average.
- Memory usage and availability.
- Disk space monitoring.
- Active systemd services inspection.

### Automated Reporting
- JSON diagnostic reports.
- Human-readable TXT reports.
- Automatic recommendations based on diagnostic results.
- Diagnostic execution error reporting.
- Timestamped report generation.

### Automated Testing
- Pytest test suite.
- Recommendation engine validation.
- Memory and disk threshold testing.
- Diagnostic error handling tests.

## Technologies

- Python 3.14.4
- Linux
- Networking and TCP/IP
- DNS
- ICMP
- Socket Programming
- systemd
- Pytest
- Git

## Project Structure

```text
it-troubleshooting-toolkit/
├── diagnostics/
│   └── report_manager.py
├── linux/
│   ├── cpu_diagnostics.py
│   ├── disk_diagnostics.py
│   ├── memory_diagnostics.py
│   └── service_diagnostics.py
├── network/
│   └── network_diagnostics.py
├── windows/
├── reports/
├── tests/
│   └── test_recommendations.py
├── main.py
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/it-troubleshooting-toolkit.git
cd it-troubleshooting-toolkit
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Install Pytest:

```bash
python3 -m pip install pytest
```

## Usage

Run the main application:

```bash
python3 main.py
```

Available menu options:

1. Network Diagnostics
2. Linux Diagnostics
3. Windows Diagnostics
4. Generate Reports
0. Exit

Generated reports are saved in the `reports/` directory.

## Running Tests

Run the automated test suite:

```bash
python3 -m pytest -v
```

Current test coverage includes:
- Healthy system conditions.
- High and critical memory usage.
- High and critical disk usage.
- Disk warning and critical states.
- Diagnostic execution errors.
- Inactive services.

## Development Environment

Developed and tested in an Ubuntu Server virtual machine running on VirtualBox.

## Roadmap

- [ ] Windows diagnostics using PowerShell.
- [ ] Process monitoring.
- [ ] Linux log analysis.
- [ ] Additional network troubleshooting tools.
- [ ] Expanded automated test coverage.

---

# IT Troubleshooting Toolkit

## Português

Uma ferramenta de diagnóstico desenvolvida em Python para auxiliar em atividades de suporte técnico, análise de sistemas e troubleshooting de infraestrutura de TI.

O projeto disponibiliza ferramentas de linha de comando para diagnosticar conectividade de rede e recursos de sistemas Linux, gerar relatórios técnicos e produzir recomendações automáticas com base nos resultados dos diagnósticos.

### Funcionalidades implementadas

**Diagnóstico de Rede**
- Teste de conectividade ICMP.
- Verificação de resolução DNS.
- Identificação do gateway padrão.
- Teste de conectividade TCP em portas específicas.

**Diagnóstico Linux**
- Informações de CPU e Load Average.
- Monitoramento de memória.
- Verificação de espaço em disco.
- Listagem de serviços ativos do systemd.

**Relatórios Automatizados**
- Geração de relatórios JSON e TXT.
- Recomendações automáticas.
- Identificação de erros durante os diagnósticos.
- Registro de data e horário.

**Testes Automatizados**
- Testes com Pytest.
- Validação das recomendações.
- Verificação dos limites de memória e disco.
- Tratamento de erros.

### Tecnologias
- Python
- Linux
- Redes de computadores
- TCP/IP
- DNS
- ICMP
- Socket Programming
- systemd
- Pytest
- Git

### Próximas implementações
- Diagnóstico Windows com PowerShell.
- Monitoramento de processos.
- Análise de logs Linux.
- Novas ferramentas de troubleshooting de rede.

## Author

Caio Silva

