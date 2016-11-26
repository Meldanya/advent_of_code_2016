# Running Haskell programs

The easiest way to get up and running with Haskell is to install
`haskell-platform`, it includes (among other things) the [GHC
compiler](https://www.haskell.org/ghc/), the [Cabal build
system](https://www.haskell.org/cabal/), and a couple of widely used
[packages](https://www.haskell.org/platform/contents.html). It should be
available in your package manager of choice, e.g. Homebrew:

```
$ brew cask install haskell-platform
```

Or `apt-get`:

```
$ sudo apt-get install haskell-platform
```

Once it's installed, you can either compile the program with GCH and run
the binary:

```
$ ghc filename.hs
$ ./filename
```

Alternatively, `haskell-platform` comes with this handy program called
`runhaskell` that combines these two steps into a single one:

```
$ runhaskell filename.hs
```
