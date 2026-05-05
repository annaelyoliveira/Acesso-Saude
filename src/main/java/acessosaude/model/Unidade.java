package acessosaude.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "unidade")
@Data
public class Unidade {
    @Id
    @Column(name = "co_cnes")
    private String coCnes;

    @Column(name = "no_fantasia")
    private String noFantasia;

    @Column(name = "tp_unidade")
    private String tpUnidade;

    @ManyToOne
    @JoinColumn(name = "turno_id")
    private Turno turno;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "endereco_id")
    private Endereco endereco;
}