package acessosaude.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "tipos_unidade")
@Data
public class TipoUnidade {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String nome; // Ex: "UNIDADE BASICA DE SAUDE", "HOSPITAL"
}
