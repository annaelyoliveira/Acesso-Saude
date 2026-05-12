package acessosaude.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Entity
@Table(name = "tb_profissionais")
@Data
public class Profissional {

    @Id
    @Column(name = "CO_PROFISSIONAL_SUS")
    private String id;

    @Column(name = "NO_PROFISSIONAL")
    private String nome;

    @Column(name = "CO_CNS")
    private String cns;
}