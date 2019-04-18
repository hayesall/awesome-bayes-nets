# Contributing

We have adopted the [*Contributor Code of Covenant*](.github/CODE_OF_CONDUCT.md).
Please read and follow these!

- Did you notice a *paper is missing*?
- Would you have found a paper sooner if this was *organized* in another way?
- Is there a feature that would improve this list?

Please help us expand this list by opening [Issues](https://github.com/batflyer/awesome-bayes-nets/issues)
or forking/sending a [Pull Request](https://github.com/batflyer/awesome-bayes-nets/pulls)
with a `.bib` file.

- Instructions for Issues are in the [Issues Template](.github/ISSUE_TEMPLATE.md)
- Instructions for Pull Requests are in the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md)

## Updating `README.md`

### Making Changes

*__Do not modify__* the `README.md` at the base of the repository.

- To change a citation, adjust the corresponding file in the `bib/` folder.
- To change anything else, adjust the `static/README.md` file.

`static/README.md` is a template that the main file is built from. This is
done by injecting citations built from `.bib` files.

### Building

Once you have added `.bib` files or modified `static/README.md`, make sure
you have the necessary Python dependencies:

```bash
$ pip install -r src/requirements.txt
```

Then build a new copy using the Makefile:

```bash
make clean
make
```

Additional notes on the build process are located in the [`src/` directory](src/).

## Mission

The original [Bayesian Networks Repository](http://www.cs.huji.ac.il/~galel/Repository/)
laid out the mission statement below.

We hope to incorporate many of these elements if possible. But our primary goal
is to *organize the landscape of research on Bayesian Networks.*

> The intention is to construct a repository that will allow us to do empirical
research within our community by facilitating (1) better reproducibility of
results, and (2) better comparisons among competing approaches. Both of these
are required to measure progress on problems that are commonly agreed upon,
such as inference and learning.
>
> A motivation for this repository is outlined in "[Challenge: Where is the Impact
of Bayesian Networks in Learning?](https://www.cs.huji.ac.il/~nir/Papers/FHGR.pdf)"
by N. Friedman, M. Goldszmidt, D. Heckerman, and S. Russell (IJCAI-97).
>
> This will be achieved by several progressive steps:
>
> 1. **Sharing domains**. This would allow for reproduction of results, and also
allow researchers in the community to run large scale empirical tests.
>
> 2. **Sharing task specification**. Sharing domains is not enough to compare
algorithms. Thus, even if two papers examine inference in a particular network,
they might be answering different queries or assuming different evidence sets.
The intent here is to store specific tasks. For example, in inference this
might be a specific series of observations/queries. In learning, this might be
a particular collection of training sets that have a particular pattern of
missing data.
>
> 3. **Sharing task evaluation**. Even if two researchers examine the same task,
they might use different measures to evaluate their algorithms. By sharing
evaluation methods, we hope to allow for an objective comparison. In some cases
such evaluation methods can be shared programs, such as a program the evaluates
the quality of learned model by computing KL divergence to the "real"
distribution. In other cases, such an evaluation method might be an agreed upon
evaluation of performance, such as space requirements, number of floating point
operations, etc.
>
> 4. **Organized competitions**. One of the dangers of empirical research is that
the methods examined become overly tuned to specific evaluation domains. To
avoid that danger, it is necessary to use "fresh" problems. The intention is to
organize competitions that would address a specific problems, such as causal
discovery, on unseen domains.

## New Topics

Because of the architecture, creating new topics is as simple as listing
a topic in the `.bib` file for a paper.

But before you do, make sure you ask yourself: **are the existing topics
truly insufficient to describe what this paper does?**

## Is this actually an [awesome-list](https://awesome.re)?

*Not technically*. The [Requirements for Awesome list(s)](https://github.com/sindresorhus/awesome/blob/master/pull_request_template.md#requirements-for-your-awesome-list)
specifically require:

> Non-generated Markdown file in a GitHub repo.

We generate a significant portion of our list from `.bib` files.
