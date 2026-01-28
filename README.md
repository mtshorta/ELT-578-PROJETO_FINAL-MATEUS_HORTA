# ELT-578 – Projeto Final | Visão Computacional

Aluno: Mateus Rabelo Horta
Disciplina: ELT 578 – Análise de Imagens e Visão Computacional
Curso: Pós-Graduação em Inteligência Artificial
Instituição: Universidade Federal de Viçosa (UFV)

## Descrição do Projeto

Este repositório contém o projeto final desenvolvido para a disciplina ELT 578 – Análise de Imagens e Visão Computacional, cujo objetivo é a implementação de um sistema de detecção automática de objetos utilizando técnicas de visão computacional e redes neurais profundas.

O projeto foi concebido como uma base genérica e extensível para aplicações industriais e profissionais de monitoramento visual. Como estudo de caso ilustrativo, foi implementada a detecção da classe dog, associada à possibilidade de geração de um alerta sonoro quando o objeto é identificado em um ambiente monitorado.

## Objetivos

Desenvolver um sistema de detecção de objetos em tempo real utilizando visão computacional

Aplicar modelos de redes neurais convolucionais pré-treinados

Demonstrar a viabilidade de soluções de baixo custo para monitoramento automatizado

Criar uma base escalável para aplicações industriais e profissionais

## Abordagem Utilizada

O sistema utiliza:

Aquisição de imagens por meio de webcam

Processamento de imagens com a biblioteca OpenCV

Detecção de objetos com o modelo SSD (Single Shot Detector)

Arquitetura MobileNet, visando eficiência computacional

Base de dados COCO, para classes de objetos

A detecção de cães é utilizada apenas como um exemplo didático, sendo possível adaptar facilmente o sistema para outras classes de interesse.

## ⚙️ Requisitos

Python 3.10+
OpenCV
NumPy


## Resultados

O sistema é capaz de:

Detectar objetos em tempo real

Delimitar objetos por meio de caixas envolventes

Classificar objetos de acordo com classes definidas

Operar com desempenho adequado em hardware convencional

Uma imagem de exemplo da detecção foi incluída no relatório acadêmico, demonstrando a correta identificação do objeto de interesse.

## Possíveis Extensões

Integração com sistemas embarcados (Raspberry Pi, Jetson)

Expansão para múltiplas classes industriais

Integração com sistemas de automação e IoT

Armazenamento de eventos e logs de detecção

Alertas visuais, sonoros ou remotos

## Contexto Acadêmico

Este projeto foi desenvolvido exclusivamente para fins acadêmicos, como parte da avaliação final da disciplina ELT 578 – Análise de Imagens e Visão Computacional, servindo como demonstração prática da aplicação de conceitos estudados ao longo do curso.
