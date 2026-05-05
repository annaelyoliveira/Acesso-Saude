package acessosaude.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "cidade")
@Data
public class Cidade {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nome;
    private String uf;
}