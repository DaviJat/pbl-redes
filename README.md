# Implementação de Sistema de Venda de Passagens Aéreas para Companhias Low-Cost com Comunicação TCP/IP e Infraestrutura em Docker

Davi Jatobá Galdino, Gabriel Sena Barbosa  
Universidade Estadual de Feira de Santana (UEFS)  
Av. Transnordestina, s/n, Novo Horizonte - BA, 44036-900  
ddavijatoba33@gmail.com, gabriel.sena.barbosa@gmail.com

**Abstract:** The low-cost carrier (LCC) sector has transformed the air transportation industry, making air travel more accessible to a larger audience. In this context, there is a growing need for a system that streamlines the ticket purchasing process, enabling users to select various flight segments. This work presents the development of a system that utilizes a TCP/IP-based API to facilitate ticket purchases. The system is designed with basic Socket API support and aims to manage multiple simultaneous requests, ensuring the integrity of reservations. Users will be able to purchase tickets efficiently, providing a seamless purchasing experience.

**Resumo:** O setor de aviação de baixo custo, ou low-cost carriers (LCCs), tem transformado a indústria do transporte aéreo, permitindo que mais pessoas tenham acesso a viagens a preços acessíveis. Nesse cenário, surge a necessidade de criar um sistema que facilite a compra de passagens, permitindo a seleção de diferentes trechos de voo. Este trabalho apresenta o desenvolvimento de um sistema que utiliza uma API baseada no subsistema de rede TCP/IP para permitir a compra de passagens. O sistema será implementado com suporte à API Socket básica e projetado para gerenciar múltiplas requisições simultâneas, garantindo a integridade das reservas. Os usuários poderão realizar compras de passagens de forma eficiente, proporcionando uma experiência de compra fluida.

## 1. Introdução

Nos últimos anos, o setor de aviação de baixo custo, ou low-cost carriers (LCCs), tem transformado a indústria do transporte aéreo, permitindo que um número maior de pessoas tenha acesso a viagens a preços acessíveis. A implementação de estratégias eficientes de redução de custos, como o uso de aeroportos secundários, maior utilização de aeronaves, tarifas sem serviços adicionais incluídos, e a automatização de operações simplificadas pela internet, não só democratizou o transporte aéreo como impulsionou o turismo e a conectividade global.

Nesse contexto, foi apresentado aos estudantes de TEC 502 (MI - Concorrência e Conectividade) o desafio de projetar e implementar um sistema que permita a compra de passagens por meio da escolha de diferentes trechos de voo, considerando a preferência de quem realizar a compra primeiro. Ficou decidido que o sistema deve ser implementado com base no subsistema de rede TCP/IP, onde o protocolo de comunicação deve ser definido de acordo com uma API especificada pela equipe de desenvolvimento. Esta API deverá ser programada em qualquer linguagem com suporte à API Socket básica do TCP/IP, visando oferecer as funcionalidades necessárias para a comunicação entre os clientes e o servidor.

Além de lidar com as questões técnicas da comunicação entre cliente e servidor, o projeto deve ser capaz de gerenciar múltiplas requisições simultâneas, assegurando que os primeiros clientes a realizarem suas compras tenham prioridade nos trechos selecionados, mantendo a integridade das suas reservas.

A abordagem adotada pela equipe de desenvolvimento seguiu a metodologia Problem-Based Learning (PBL), que se concentra na resolução de problemas reais como forma de aprendizado. Este relatório deverá documentar o processo de desenvolvimento, apresentando as decisões tomadas e os conceitos teóricos que fundamentam a programação de um software desse tipo, evidenciando a conexão entre teoria e prática ao longo do projeto.
