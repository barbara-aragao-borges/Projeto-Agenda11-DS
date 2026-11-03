
# 💧 Sistema de Controle de Níveis de Água

## 1. Sobre o projeto

Este projeto foi desenvolvido utilizando a linguagem Python.

O objetivo é criar um sistema simples de monitoramento de um reservatório de água, capaz de identificar diferentes níveis de armazenamento e exibir mensagens de alerta coloridas no terminal, de acordo com a situação identificada.

Para destacar visualmente cada situação, foi utilizada a biblioteca **Colorama**, que permite aplicar cores às mensagens exibidas no terminal.

## 2. Funcionalidades

O programa apresenta cinco níveis de água, cada um associado a uma situação e a uma cor específica:

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

O sistema percorre automaticamente os cinco níveis, apresenta as mensagens correspondentes e restaura a formatação padrão do terminal após cada exibição.

## 3. Tecnologias e recursos utilizados

- **Python:** linguagem de programação utilizada no desenvolvimento do sistema.
- **Colorama:** biblioteca utilizada para personalizar as cores das mensagens no terminal.
- **Listas:** utilizadas para armazenar as situações do reservatório.
- **Funções:** utilizadas para organizar o código e definir a cor correspondente a cada nível.
- **Estrutura de repetição FOR:** utilizada para percorrer os níveis armazenados na lista.
- **Estruturas condicionais IF e ELIF:** utilizadas para verificar o nível informado e determinar sua respectiva cor.

## 4. Organização e lógica do programa

O código foi organizado em etapas para facilitar a compreensão e a manutenção:

**1. Importação da biblioteca**

São importados os recursos `Fore`, `Style` e `init`, disponibilizados pela biblioteca Colorama, permitindo a aplicação de cores e a restauração da formatação do terminal.

**2. Criação da lista**

Foi criada uma lista chamada `niveis`, contendo as cinco situações possíveis do reservatório, organizadas em ordem crescente.

**3. Criação da função definir_cor()**

A função recebe o número do nível como parâmetro e utiliza estruturas condicionais para retornar a cor correspondente.

**4. Simulação do monitoramento**

A estrutura de repetição `FOR` percorre os cinco níveis, utilizando a função `len()` para identificar a quantidade de elementos da lista e `range()` para gerar os números dos níveis.

**5. Exibição das mensagens**

O programa utiliza a função `print()` para apresentar o nível e sua respectiva situação com a cor definida. O recurso `Style.RESET_ALL` restaura a formatação padrão após cada mensagem.

## 5. Requisitos para execução

Para executar o projeto, é necessário ter:

- Python instalado no computador.
- Biblioteca Colorama instalada.
- Um editor de código ou terminal compatível com Python.

### Instalação da biblioteca

Execute o seguinte comando no terminal:

```bash
pip install colorama
```

## 6. Como executar o programa

1. Faça o download ou clone deste repositório.
2. Abra a pasta do projeto no Visual Studio Code ou em outro editor de código.
3. Verifique se a biblioteca Colorama está instalada.
4. Execute o arquivo `main.py`.

Comando para execução:

```bash
python main.py
```

## 7. Resultado esperado

Ao executar o programa, serão exibidas cinco mensagens no terminal, cada uma identificada pelo número do nível do reservatório, sua respectiva situação e a cor correspondente.

## 8. Referencias

Materiais da aula da agenda 11 de DS.