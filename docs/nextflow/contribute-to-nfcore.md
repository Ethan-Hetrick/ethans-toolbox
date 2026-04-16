# Contributing to nf-core

Follow the official [nf-core contribution documentation](https://nf-co.re/docs/contributing/how_to_contribute_to_nf-core) for the full process. This page is a short working checklist.

1. Create a fork or branch for the nf-core repository you want to change, for example [nf-core/modules](https://github.com/nf-core/modules/tree/master).
2. Make your changes and follow the [nf-core component guidelines](https://nf-co.re/docs/tutorials/nf-core_components/components), including the [module guidelines](https://nf-co.re/docs/guidelines/components/modules).
3. Test your changes. Example:

   ```bash
   nf-test test modules/nf-core/fastani/tests/main.nf.test --profile +singularity --verbose --update-snapshot
   ```

4. Update the `meta.yml`.
5. Run the appropriate linting command. Example:

   ```bash
   nf-core modules lint --dir modules/nf-core/fastani
   ```

6. Open a pull request, fill out the required fields, and confirm the checks pass.
