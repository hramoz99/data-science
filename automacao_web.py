{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Automação Web e Busca de Informações com Python\n",
    "\n",
    "#### Desafio: \n",
    "\n",
    "Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:\n",
    "- Dólar\n",
    "- Euro\n",
    "- Ouro\n",
    "\n",
    "Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.\n",
    "\n",
    "Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing\n",
    "\n",
    "Para isso, vamos criar uma automação web:\n",
    "\n",
    "- Usaremos o selenium\n",
    "- Importante: baixar o webdriver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.219799999999999\n",
      "6.1283583880000005\n",
      "294.15\n"
     ]
    }
   ],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "\n",
    "# para rodar o chrome em 2º plano\n",
    "# from selenium.webdriver.chrome.options import Options\n",
    "# chrome_options = Options()\n",
    "# chrome_options.headless = True \n",
    "# navegador = webdriver.Chrome(options=chrome_options)\n",
    "\n",
    "# abrir um navegador\n",
    "navegador = webdriver.Chrome()\n",
    "\n",
    "navegador.get(\"https://www.google.com/\")\n",
    "\n",
    "# Passo 1: Pegar a cotação do Dólar\n",
    "navegador.find_element_by_xpath(\n",
    "    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(\"cotação dólar\")\n",
    "\n",
    "navegador.find_element_by_xpath(\n",
    "    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)\n",
    "\n",
    "cotacao_dolar = navegador.find_element_by_xpath(\n",
    "    '//*[@id=\"knowledge-currency__updatable-data-column\"]/div[1]/div[2]/span[1]').get_attribute(\"data-value\") \n",
    "print(cotacao_dolar)\n",
    "\n",
    "# Passo 2: Pegar a cotação do Euro\n",
    "navegador.get(\"https://www.google.com/\")\n",
    "navegador.find_element_by_xpath(\n",
    "    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(\"cotação euro\")\n",
    "navegador.find_element_by_xpath(\n",
    "    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)\n",
    "\n",
    "cotacao_euro = navegador.find_element_by_xpath(\n",
    "    '//*[@id=\"knowledge-currency__updatable-data-column\"]/div[1]/div[2]/span[1]').get_attribute(\"data-value\")\n",
    "print(cotacao_euro)\n",
    "\n",
    "# Passo 3: Pegar a cotação do Ouro\n",
    "navegador.get(\"https://www.melhorcambio.com/ouro-hoje\")\n",
    "\n",
    "cotacao_ouro = navegador.find_element_by_xpath('//*[@id=\"comercial\"]').get_attribute(\"value\")\n",
    "cotacao_ouro = cotacao_ouro.replace(\",\", \".\")\n",
    "print(cotacao_ouro)\n",
    "\n",
    "navegador.quit()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Agora vamos atualiza a nossa base de preços com as novas cotações"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Importando a base de dados"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Produtos</th>\n",
       "      <th>Preço Original</th>\n",
       "      <th>Moeda</th>\n",
       "      <th>Cotação</th>\n",
       "      <th>Preço de Compra</th>\n",
       "      <th>Margem</th>\n",
       "      <th>Preço de Venda</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Câmera Canon</td>\n",
       "      <td>999.99</td>\n",
       "      <td>Dólar</td>\n",
       "      <td>5</td>\n",
       "      <td>4999.95</td>\n",
       "      <td>1.40</td>\n",
       "      <td>6999.930</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Carro Renault</td>\n",
       "      <td>4500.00</td>\n",
       "      <td>Euro</td>\n",
       "      <td>6</td>\n",
       "      <td>27000.00</td>\n",
       "      <td>2.00</td>\n",
       "      <td>54000.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Notebook Dell</td>\n",
       "      <td>899.99</td>\n",
       "      <td>Dólar</td>\n",
       "      <td>5</td>\n",
       "      <td>4499.95</td>\n",
       "      <td>1.70</td>\n",
       "      <td>7649.915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IPhone</td>\n",
       "      <td>799.00</td>\n",
       "      <td>Dólar</td>\n",
       "      <td>5</td>\n",
       "      <td>3995.00</td>\n",
       "      <td>1.70</td>\n",
       "      <td>6791.500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Carro Fiat</td>\n",
       "      <td>3000.00</td>\n",
       "      <td>Euro</td>\n",
       "      <td>6</td>\n",
       "      <td>18000.00</td>\n",
       "      <td>1.90</td>\n",
       "      <td>34200.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Celular Xiaomi</td>\n",
       "      <td>480.48</td>\n",
       "      <td>Dólar</td>\n",
       "      <td>5</td>\n",
       "      <td>2402.40</td>\n",
       "      <td>2.00</td>\n",
       "      <td>4804.800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Joia 20g</td>\n",
       "      <td>20.00</td>\n",
       "      <td>Ouro</td>\n",
       "      <td>350</td>\n",
       "      <td>7000.00</td>\n",
       "      <td>1.15</td>\n",
       "      <td>8050.000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Produtos  Preço Original  Moeda  Cotação  Preço de Compra  Margem  \\\n",
       "0    Câmera Canon          999.99  Dólar        5          4999.95    1.40   \n",
       "1   Carro Renault         4500.00   Euro        6         27000.00    2.00   \n",
       "2   Notebook Dell          899.99  Dólar        5          4499.95    1.70   \n",
       "3          IPhone          799.00  Dólar        5          3995.00    1.70   \n",
       "4      Carro Fiat         3000.00   Euro        6         18000.00    1.90   \n",
       "5  Celular Xiaomi          480.48  Dólar        5          2402.40    2.00   \n",
       "6        Joia 20g           20.00   Ouro      350          7000.00    1.15   \n",
       "\n",
       "   Preço de Venda  \n",
       "0        6999.930  \n",
       "1       54000.000  \n",
       "2        7649.915  \n",
       "3        6791.500  \n",
       "4       34200.000  \n",
       "5        4804.800  \n",
       "6        8050.000  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Passo 4: Importar a lista de produtos\n",
    "import pandas as pd\n",
    "\n",
    "tabela = pd.read_excel(\"Produtos.xlsx\")\n",
    "display(tabela)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Atualizando os preços e o cálculo do Preço Final"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Produtos</th>\n",
       "      <th>Preço Original</th>\n",
       "      <th>Moeda</th>\n",
       "      <th>Cotação</th>\n",
       "      <th>Preço de Compra</th>\n",
       "      <th>Margem</th>\n",
       "      <th>Preço de Venda</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Câmera Canon</td>\n",
       "      <td>999.99</td>\n",
       "      <td>Dólar</td>\n",
       "      <td>5.219800</td>\n",
       "      <td>5219.747802</td>\n",
       "      <td>1.40</td>\n",
       "      <td>7307.646923</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Carro Renault</td>\n",
       "      <td>4500.00</td>\n",
       "      <td>Euro</td>\n",
       "      <td>6.128358</td>\n",
       "      <td>27577.612746</td>\n",
       "      <td>2.00</td>\n",
       "      <td>55155.225492</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Notebook Dell</td>\n",
       "      <td>899.99</td>\n",
       "      <td>Dólar</td>\n",
       "      <td>5.219800</td>\n",
       "      <td>4697.767802</td>\n",
       "      <td>1.70</td>\n",
       "      <td>7986.205263</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IPhone</td>\n",
       "      <td>799.00</td>\n",
       "      <td>Dólar</td>\n",
       "      <td>5.219800</td>\n",
       "      <td>4170.620200</td>\n",
       "      <td>1.70</td>\n",
       "      <td>7090.054340</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Carro Fiat</td>\n",
       "      <td>3000.00</td>\n",
       "      <td>Euro</td>\n",
       "      <td>6.128358</td>\n",
       "      <td>18385.075164</td>\n",
       "      <td>1.90</td>\n",
       "      <td>34931.642812</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Celular Xiaomi</td>\n",
       "      <td>480.48</td>\n",
       "      <td>Dólar</td>\n",
       "      <td>5.219800</td>\n",
       "      <td>2508.009504</td>\n",
       "      <td>2.00</td>\n",
       "      <td>5016.019008</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Joia 20g</td>\n",
       "      <td>20.00</td>\n",
       "      <td>Ouro</td>\n",
       "      <td>294.150000</td>\n",
       "      <td>5883.000000</td>\n",
       "      <td>1.15</td>\n",
       "      <td>6765.450000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Produtos  Preço Original  Moeda     Cotação  Preço de Compra  Margem  \\\n",
       "0    Câmera Canon          999.99  Dólar    5.219800      5219.747802    1.40   \n",
       "1   Carro Renault         4500.00   Euro    6.128358     27577.612746    2.00   \n",
       "2   Notebook Dell          899.99  Dólar    5.219800      4697.767802    1.70   \n",
       "3          IPhone          799.00  Dólar    5.219800      4170.620200    1.70   \n",
       "4      Carro Fiat         3000.00   Euro    6.128358     18385.075164    1.90   \n",
       "5  Celular Xiaomi          480.48  Dólar    5.219800      2508.009504    2.00   \n",
       "6        Joia 20g           20.00   Ouro  294.150000      5883.000000    1.15   \n",
       "\n",
       "   Preço de Venda  \n",
       "0     7307.646923  \n",
       "1    55155.225492  \n",
       "2     7986.205263  \n",
       "3     7090.054340  \n",
       "4    34931.642812  \n",
       "5     5016.019008  \n",
       "6     6765.450000  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Passo 5: Recalcular o preço de cada produto\n",
    "# atualizar a cotação\n",
    "# nas linhas onde na coluna \"Moeda\" = Dólar\n",
    "tabela.loc[tabela[\"Moeda\"] == \"Dólar\", \"Cotação\"] = float(cotacao_dolar)\n",
    "tabela.loc[tabela[\"Moeda\"] == \"Euro\", \"Cotação\"] = float(cotacao_euro)\n",
    "tabela.loc[tabela[\"Moeda\"] == \"Ouro\", \"Cotação\"] = float(cotacao_ouro)\n",
    "\n",
    "# atualizar o preço base reais (preço base original * cotação)\n",
    "tabela[\"Preço de Compra\"] = tabela[\"Preço Original\"] * tabela[\"Cotação\"]\n",
    "\n",
    "# atualizar o preço final (preço base reais * Margem)\n",
    "tabela[\"Preço de Venda\"] = tabela[\"Preço de Compra\"] * tabela[\"Margem\"]\n",
    "\n",
    "# tabela[\"Preço de Venda\"] = tabela[\"Preço de Venda\"].map(\"R${:.2f}\".format)\n",
    "\n",
    "display(tabela)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Agora vamos exportar a nova base de preços atualizada"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Passo 6: Salvar os novos preços dos produtos\n",
    "tabela.to_excel(\"Produtos Novo.xlsx\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
