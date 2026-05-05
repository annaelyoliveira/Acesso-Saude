package acessosaude.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "estabelecimentos")
@Data
public class Estabelecimento {
    @Id
    @Column(name = "co_cnes")
    private String coCnes;

    private String noFantasia;
    private String tpUnidade;
    private String turnoAtendimento;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "endereco_id")
    private Endereco endereco;
}
