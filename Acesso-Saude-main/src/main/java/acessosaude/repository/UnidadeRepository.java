package acessosaude.repository;

import acessosaude.model.Unidade;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.stereotype.Repository;

@Repository
public interface UnidadeRepository
        extends JpaRepository<Unidade, String>,
        JpaSpecificationExecutor<Unidade> {
}