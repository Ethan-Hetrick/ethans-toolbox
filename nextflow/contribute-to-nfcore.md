# Contributing to nf-core procedure

*Follow the [Contributions documentation](https://nf-co.re/docs/contributing/how_to_contribute_to_nf-core)*

1) Create a fork or branch of the nf-core repo you want to contribute to. e.g. [nf-core modules](https://github.com/nf-core/modules/tree/master)
2) Make your changes. Follow the [nf-core component guidelines](https://nf-co.re/docs/tutorials/nf-core_components/components). e.g. [module guidelines](https://nf-co.re/docs/guidelines/components/modules)
3) Test your changes. Here is an example of testing a module `nf-test test modules/nf-core/fastani/tests/main.nf.test --profile +singularity --verbose --update-snapshot`
4) Update the `meta.yml`
5)  Use appropriate linting tool. E.g. `nf-core modules lint --dir modules/nf-core/ fastani`
6)  Create a PR and fill out required fields. Check to see if changes passed tests
