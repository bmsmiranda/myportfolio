/*  
  Seleção PNPD 088-2020  
  Autor/Candidato: Bruno Miranda (bmsmiranda@gmail.com)
  Github: https://github.com/bmsmiranda/myportfolio/tree/main/IPEA

  Data: 
	09-10-2020 - criação do script
*/

/***  Análise de registros em base fictícia Ipea 2020  ***/
-- Objetivo: responder questionamentos do teste aplicado

use BANCO;
go

select count(*) from teste
select distinct(orgao) from teste order by orgao

-- Pergunta 1
-- Resposta: opção não encontrada para seleção
select 
  count(*)
from 
  teste
where
  1 = 1
  and sexo = 'M'
  and idade > 50
  and uf = 'BA'
  and ano = '2019'
-------------------------------------------------------------------------------

-- Pergunta 2
-- Resposta: 2017 - ABC
select 
  ano, orgao, count(*) as qtd
from 
  teste
where
  1 = 1
  and sexo = 'F'  
group by
  ano
  , orgao
order by 
  qtd desc
-------------------------------------------------------------------------------

-- pergunta 3
-- Resposta: nenhuma das alternativas
declare @count decimal(8, 2);
set @count = cast((select count(*) from teste where orgao = 'Ipea' and ano = '2015' and (escolaridade is not null and escolaridade != '')) as decimal)

select 
  escolaridade
  , count(*) as qtd_esc
  , @count as qtd_total
  , ((CONVERT(decimal, (count(*))) / @count) * 100) as perc
from teste
where
  1 = 1 
  and orgao = 'Ipea'  
  and escolaridade = 4
  and ano = '2015'
  and (escolaridade is not null and escolaridade != '')
group by
  escolaridade
order by 
  escolaridade asc
-------------------------------------------------------------------------------

-- Pergunta 4
-- Resposta: Amarelo com 30 registros
select 
  raca, count(*) as qtd
from teste
where
  1 = 1
  and sexo = 'F'  
  and ano = '2010'
  and orgao = 'UFSJ'
  and (raca is not null and raca != '')
group by
  raca
order by 
  qtd asc
-------------------------------------------------------------------------------

-- Pergunta 5
-- demonstra o quantitativo de funcionários segmentado por genero por ano
select 
  ano
  , sexo
  , count(*) as qtd 
from 
  teste
where
  1 = 1
  and ano between '1985' and '2019' 
  and (sexo is not null and sexo != '') 
group by 
  ano
  , sexo

-- demonstra percentual de funcionários segmentado por raça durante toda a série
select 
  ano
  , raca
  , count(*) as qtd 
from 
  teste
where
  1 = 1
  and ano between '1985' and '2019' 
  and (sexo is not null and sexo != '')
group by
  ano
  , raca

-- demonstra a média da remuneraçao segmento pela variável genero
select
  ano
  , sexo
  , AVG(CONVERT(numeric(8, 1), remuneracao)) as mediaremuneracao
from
  teste 
where 
  1 = 1  
  and ano between '1985' and '2019' 
  and (sexo is not null and sexo != '') group by ano, sexo
-------------------------------------------------------------------------------