package acessosaude.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "endereco")
@Data
public class Endereco {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String logradouro;
    private String bairro;
    private String cep;

    @ManyToOne
    @JoinColumn(name = "cidade_id")
    private Cidade cidade;
}