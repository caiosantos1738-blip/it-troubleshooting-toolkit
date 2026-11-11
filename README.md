# IT Troubleshooting Toolkit

[![Python](https://img.shields.io/badge/Python-3.14.4-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-yellow?logo=linux&logoColor=white)](https://www.linux.org/)
[![Tests](https://img.shields.io/badge/Tests-Pytest-green?logo=pytest&logoColor=white)](https://pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

**A command-line toolkit for IT troubleshooting, network diagnostics, and Linux system monitoring.**

IT Troubleshooting Toolkit is a Python-based project designed to assist IT support and infrastructure professionals with common diagnostic tasks.

It provides network connectivity tests, Linux system resource monitoring, automated technical reports, and rule-based recommendations.

The project was developed as a practical learning experience focused on Help Desk, IT Infrastructure, and troubleshooting operations.

## Features

### Network Diagnostics
- ICMP connectivity testing using ping.
- DNS resolution and IP address lookup.
- Default gateway detection.
- TCP port connectivity testing.

### Linux System Diagnostics
- CPU model, logical cores, and system load averages.
- Memory usage and available memory.
- Disk space monitoring and usage thresholds.
- Active systemd services inspection.

### Automated Reporting
- JSON diagnostic report generation.
- Human-readable TXT reports.
- Automatic recommendations based on diagnostic results.
- Diagnostic error identification.
- Timestamped report files.

### Automated Testing
- Pytest test suite.
- Recommendation engine validation.
- Memory and disk usage threshold testing.
- Diagnostic error handling.
- Disk warning and critical status validation.

## Technologies

| Technology | Purpose |
|---|---|
| Python 3.14.4 | Main programming language |
| Linux | Development and testing environment |
| TCP/IP | Network diagnostics |
| DNS | Name resolution |
| ICMP | Connectivity testing |
| Socket Programming | TCP connection testing |
| systemd | Linux service inspection |
| Pytest | Automated testing |
| Git and GitHub | Version control |

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

### Prerequisites

- Linux environment.
- Python 3.10 or newer.
- Git.
- System utilities such as `ping`, `ip`, `free`, `lscpu`, and `systemctl`.

### 1. Clone the repository

```bash
git clone https://github.com/caiosantos1738-blip/it-troubleshooting-toolkit.git

cd it-troubleshooting-toolkit
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the environment

```bash
source .venv/bin/activate
```

### 4. Install testing dependencies

```bash
python3 -m pip install pytest
```

## Usage

Start the application:

```bash
python3 main.py
```

Available menu options:

```text
1. Network Diagnostics
2. Linux Diagnostics
3. Windows Diagnostics
4. Generate Reports
0. Exit
```

**Note:** Windows diagnostics are currently planned and not yet implemented.

### Generating Reports

Select option `4` in the main menu to execute the available Linux diagnostics and generate reports.

Reports are saved in the `reports/` directory in two formats:

- `.json` — structured diagnostic data.
- `.txt` — human-readable diagnostic summary.

The report generator also evaluates diagnostic results and provides recommendations when potential issues are detected.

## Automated Tests

Run the test suite:

```bash
python3 -m pytest -v
```

The current test suite contains **9 automated tests**, covering:

- Healthy system conditions.
- High memory usage.
- Critical memory usage.
- High disk usage.
- Critical disk usage.
- Disk warning status.
- Disk critical status.
- Diagnostic execution errors.
- Inactive services.

**Latest validation:** 9 tests passed.

## Development Environment

- Operating System: Ubuntu Server.
- Virtualization: Oracle VirtualBox.
- Language: Python 3.14.4.
- Version Control: Git and GitHub.
- Testing Framework: Pytest.

## Roadmap

- [ ] Windows diagnostics using PowerShell.
- [ ] Linux process monitoring.
- [ ] Linux log analysis.
- [ ] Additional network troubleshooting tools.
- [ ] Expanded automated test coverage.
- [ ] Documentation with execution screenshots.

## Learning Objectives

This project demonstrates practical knowledge and hands-on experience with:

- IT troubleshooting methodologies.
- Linux system administration.
- Network diagnostics and TCP/IP.
- Python scripting and automation.
- System monitoring.
- Technical report generation.
- Automated testing and version control.

## Author

**Caio Silva**

- GitHub: [@caiosantos1738-blip](https://github.com/caiosantos1738-blip)
- Project: [IT Troubleshooting Toolkit](https://github.com/caiosantos1738-blip/it-troubleshooting-toolkit)

---

# IT Troubleshooting Toolkit

## Português

**Ferramenta de linha de comando para troubleshooting de TI, diagnóstico de redes e monitoramento de sistemas Linux.**

O IT Troubleshooting Toolkit é um projeto desenvolvido em Python para auxiliar profissionais de suporte técnico e infraestrutura na execução de tarefas comuns de diagnóstico.

A ferramenta disponibiliza testes de conectividade de rede, monitoramento de recursos Linux, geração automatizada de relatórios técnicos e recomendações baseadas nos resultados.

O projeto foi desenvolvido como experiência prática de aprendizado, com foco em Help Desk, Infraestrutura de TI e resolução de problemas.

## Funcionalidades

### Diagnóstico de Rede
- Teste de conectividade ICMP com ping.
- Verificação de resolução DNS.
- Identificação do gateway padrão.
- Teste de conectividade TCP em portas específicas.

### Diagnóstico Linux
- Modelo da CPU, núcleos lógicos e Load Average.
- Monitoramento de memória.
- Monitoramento de espaço em disco.
- Inspeção de serviços ativos do systemd.

### Relatórios Automatizados
- Geração de relatórios JSON.
- Relatórios TXT legíveis.
- Recomendações automáticas.
- Identificação de erros durante os diagnósticos.
- Registro de data e horário.

### Testes Automatizados
- Testes utilizando Pytest.
- Validação do mecanismo de recomendações.
- Testes de limites de memória e disco.
- Validação de tratamento de erros.
- Verificação de estados de alerta do disco.

## Tecnologias

- Python 3.14.4.
- Linux.
- Redes de computadores.
- TCP/IP.
- DNS.
- ICMP.
- Socket Programming.
- systemd.
- Pytest.
- Git e GitHub.

## Instalação e utilização

Consulte a seção Installation para obter as instruções de instalação e execução.

Para executar os testes automatizados:

```bash
python3 -m pytest -v
```

## Próximas implementações

- [ ] Diagnóstico Windows com PowerShell.
- [ ] Monitoramento de processos Linux.
- [ ] Análise de logs Linux.
- [ ] Novas ferramentas de troubleshooting de rede.
- [ ] Ampliação dos testes automatizados.
- [ ] Documentação com capturas de tela.

## Autor

**Caio Silva**

[GitHub](https://github.com/caiosantos1738-blip) | [Repositório do projeto](https://github.com/caiosantos1738-blip/it-troubleshooting-toolkit)
