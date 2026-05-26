-- =====================================================================
-- ATIVIDADE PRÁTICA: MANIPULAÇÃO DE BANCO DE DADOS (SQL)
-- Aluno: Caio
-- =====================================================================

-- PASSO 1: Criar a tabela chamada Livros
CREATE TABLE Livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    genero TEXT NOT NULL,
    disponivel BOOLEAN NOT NULL CHECK (disponivel IN (0, 1)) -- 1 para Sim, 0 para Não
);

-- PASSO 2: Inserir 5 livros fictícios (incluindo um antigo para o Passo 6)
INSERT INTO Livros (titulo, autor, ano, genero, disponivel) VALUES 
('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 'Fantasia', 1),
('1984', 'George Orwell', 1949, 'Distopia', 0),
('Dom Casmurro', 'Machado de Assis', 1899, 'Romance', 1),
('O Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasia', 1),
('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 1997, 'Fantasia', 0);

-- PASSO 3: Selecionar todos os livros disponíveis
SELECT * FROM Livros WHERE disponivel = 1;

-- PASSO 4: Atualizar a disponibilidade de 1 livro (Mudando o ID 2 para disponível)
UPDATE Livros 
SET disponivel = 1 
WHERE id = 2;

-- PASSO 5: Listar os livros do mais recente para o mais antigo (Ordenação Decrescente)
SELECT * FROM Livros 
ORDER BY ano DESC;

-- PASSO 6: Delete um livro com ano anterior a 1940 (Vai deletar Dom Casmurro e O Hobbit)
DELETE FROM Livros 
WHERE ano < 1940;

-- PASSO 7: Apagar a tabela Livros (DROP) e depois recriá-la
DROP TABLE Livros;

-- Recriando a tabela limpa conforme solicitado no último passo
CREATE TABLE Livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    genero TEXT NOT NULL,
    disponivel BOOLEAN NOT NULL CHECK (disponivel IN (0, 1))
); 