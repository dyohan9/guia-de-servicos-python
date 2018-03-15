import guia_acesso

#Retorna os dados do json
#http://www.servicos.al.gov.br/api/v1/units/5757f1aa8c36c75fd9000003.json

id = "5757f1aa8c36c75fd9000003"

#Retorna o conteudo total "json" do api
print guia_acesso.UnitID(id, "units").getContent()

#Retorna o valor da chave "name" da Unidade
print guia_acesso.UnitID(id, "units").getUnitName()

#Retorna o valor da chave "url" da Unidade
print guia_acesso.UnitID(id, "units").getURL()

