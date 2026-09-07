# ⚡ Calculadora de Consumo de Energia Elétrica

![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub Badge](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![License Badge](https://img.shields.io/badge/Licen%C3%A7a-MIT-green?style=for-the-badge)

---

## 📌 Sobre o Projeto

O **Programa Consumo de Energia** é uma ferramenta desenvolvida em **Python** para calcular o consumo mensal estimado de energia elétrica de um eletrodoméstico, além de projetar o custo financeiro em Reais (R$) com base no tempo de uso diário e na potência do aparelho.

### 🎯 Objetivos:
- Conscientizar sobre o consumo de energia elétrica residencial.
- Fornecer uma estimativa rápida e simples do custo mensal de aparelhos individuais.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python 3](https://www.python.org/
- **Biblioteca Nativa:** `os` (para limpeza do terminal de forma simples e multiplataforma)

---

## 📐 Fórmula Utilizada

O cálculo do consumo mensal e do custo estimado utiliza as seguintes equações baseadas no código:

1. **Consumo Mensal (kWh/mês):**
   $$\text{Consumo} = \frac{\text{Horas de Uso Diário} \times 30 \text{ dias} \times \text{Potência (W)}}{1000}$$

   2. **Custo Estimado (R$):**
      $$\text{Custo Estimado} = \text{Consumo (kWh/mês)} \times 0{,}75$$

      > **Nota:** O valor de **R$ 0,75** por kWh é a taxa de conversão padrão utilizada pelo programa.

      ---
