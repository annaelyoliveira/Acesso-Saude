package acessosaude.controller;

import acessosaude.model.Unidade;
import acessosaude.repository.UnidadeRepository;
import jakarta.persistence.criteria.Predicate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/api/v1/saude")
@CrossOrigin("*")
public class UnidadeController {

    @Autowired
    private UnidadeRepository repository;

    @GetMapping("/unidades")
    public List<Unidade> buscarUnidades(

            @RequestParam(required = false) String cidade,
            @RequestParam(required = false) String bairro,
            @RequestParam(required = false) String tipo,
            @RequestParam(required = false) Integer turno,
            @RequestParam(required = false) String nome

    ) {

        return repository.findAll((root, query, cb) -> {

            List<Predicate> predicates = new ArrayList<>();

            // Cidade
            if (cidade != null && !cidade.isBlank()) {
                predicates.add(
                        cb.equal(
                                cb.upper(root.get("endereco")
                                        .get("cidade")
                                        .get("nome")),
                                cidade.toUpperCase()
                        )
                );
            }

            // Bairro
            if (bairro != null && !bairro.isBlank()) {
                predicates.add(
                        cb.equal(
                                cb.upper(root.get("endereco")
                                        .get("bairro")),
                                bairro.toUpperCase()
                        )
                );
            }

            // Tipo Unidade
            if (tipo != null && !tipo.isBlank()) {
                predicates.add(
                        cb.equal(root.get("tipoUnidade"), tipo)
                );
            }

            // Turno
            if (turno != null) {
                predicates.add(
                        cb.equal(root.get("coTurno"), turno)
                );
            }

            // Nome
            if (nome != null && !nome.isBlank()) {
                predicates.add(
                        cb.like(
                                cb.upper(root.get("nomeFantasia")),
                                "%" + nome.toUpperCase() + "%"
                        )
                );
            }

            return cb.and(predicates.toArray(new Predicate[0]));
        });
    }
}