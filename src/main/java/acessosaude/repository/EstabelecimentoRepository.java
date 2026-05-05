package acessosaude.repository;

import acessosaude.model.Estabelecimento;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface EstabelecimentoRepository extends JpaRepository<Estabelecimento, String> {

    // Consulta por Turno
    List<Estabelecimento> findByTurnoAtendimentoContainingIgnoreCase(String turno);

    // Consulta por Tipo de Unidade
    List<Estabelecimento> findByTpUnidadeContainingIgnoreCase(String tipo);

    // Consulta por Cidade e Bairro (Acessando atributos da entidade Endereco)
    List<Estabelecimento> findByEnderecoCidadeIgnoreCaseAndEnderecoBairroIgnoreCase(String cidade, String bairro);
}