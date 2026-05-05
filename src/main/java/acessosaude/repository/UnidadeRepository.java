package acessosaude.repository;

import acessosaude.model.Unidade;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface UnidadeRepository extends JpaRepository<Unidade, String> {

    // Consulta 1: Por turno (Lógica na tabela Turno)
    List<Unidade> findByTurnoDescricaoContainingIgnoreCase(String turno);

    // Consulta 2: Por tipo de unidade
    List<Unidade> findByTpUnidadeContainingIgnoreCase(String tipo);

    // Consulta 3: Por Cidade e Bairro (Navegação Unidade -> Endereço -> Cidade)
    List<Unidade> findByEnderecoCidadeNomeIgnoreCaseAndEnderecoBairroIgnoreCase(String cidade, String bairro);
}