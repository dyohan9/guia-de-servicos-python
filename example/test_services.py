import guia_acesso

#Retorna os dados do json http://www.servicos.al.gov.br/api/v1/services/5935d06c8c36c703077eddec.json

id = "5935d06c8c36c703077eddec"

#Retorna o conteudo total "json" do api
print guia_acesso.Services(id, "services").getContent()

#Retorna o valor da chave "name" do api
print guia_acesso.Services(id, "services").getName()

#Retorna a o valor da chave "description" do api
print guia_acesso.Services(id, "services").getDescription()

#Retorna o valor da chave "applicants" do api
print guia_acesso.Services(id, "services").getApplicants()

#Retorna o valor da chave 0 de "steps" do api, caso queira acessar outros dados dentro do steps passe as chaves apos a funcao
print guia_acesso.Services(id, "services").getSteps()

#Retorna o valor da chave "unit_ids" do api
print guia_acesso.Services(id, "services").getUnitID()