# CRUD REST NoSQL


| Rotas |
|---|---|
| [GET] **/posts**. Retorna todos os posts do banco de dados. |
| [GET] **/posts/\<id>**. Retorna 404 para um id não existente no banco. |
| [POST] **/posts**. Retorna o status code mais indicado caso esteja faltando alguma chave no JSON enviado. |
| [POST] **/posts**. Ao receber uma requisição correta, salva os dados no banco de dados e retorna o status 201. |
| [PATCH] **/posts/\<id>**. Retorna o status code mais indicado caso o JSON enviado não seja válido. |
| [PATCH] **/posts/\<id>**. Tentativa de editar post inexistente retorna **404**. |
| [PATCH] **/posts/\<id>**. Retorna o objeto atualizado e status **200** em caso de sucesso na atualização. |
| [DELETE] **/posts/\<id>**. Retorna o objeto deletado e o status code correto. Deletando o post indicado do banco de dados. |
| [DELETE] **/posts/\<id>**. Tentativa de deletar post inexistente retorna **404**. |
| **id auto incrementável**. A cada novo post criado o id é incrementado automaticamente. Mesmo reiniciando a aplicação. |
| **Arquitetura** e **Design Pattern**. Organização do projeto de acordo com o padrão **MVC** e uso do Design Pattern **Factory**. |
| **POO**. Utilização dos tipos corretos de atributos e métodos nas classes. (Instância, Classe, estáticos). E uso dos métodos especiais |
| **MongoDB**. Conexão com o banco seguindo boas práticas e uso correto das funções disponibilizadas pelo **Pymongo**. |
