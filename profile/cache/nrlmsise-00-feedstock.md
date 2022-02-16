About nrlmsise-00
=================

Home: https://www.brodo.de/space/nrlmsise/

Package license: 

Feedstock license: [BSD-3-Clause](https://github.com/tudat-team/feedstock-feedstock/blob/master/LICENSE.txt)

Summary: The NRLMSIS-00 empirical atmosphere model

The NRLMSIS-00 empirical atmosphere model was developed by Mike
Picone, Alan Hedin, and Doug Drob based on the MSISE90 model.

The MSISE90 model describes the neutral temperature and densities in
Earth's atmosphere from ground to thermospheric heights. Below 72.5 km
the model is primarily based on the MAP Handbook (Labitzke et al.,
1985) tabulation of zonal average temperature and pressure by Barnett
and Corney, which was also used for the CIRA-86. Below 20 km these
data were supplemented with averages from the National Meteorological
Center (NMC). In addition, pitot tube, falling sphere, and grenade
sounder rocket measurements from 1947 to 1972 were taken into
consideration. Above 72.5 km MSISE-90 is essentially a revised MSIS-86
model taking into account data derived from space shuttle flights and
newer incoherent scatter results. For someone interested only in the
thermosphere (above 120 km), the author recommends the MSIS-86
model. MSISE is also not the model of preference for specialized
tropospheric work. It is rather for studies that reach across several
atmospheric boundaries.
(quoted from http://nssdc.gsfc.nasa.gov/space/model/atmos/nrlmsise00.html)


Current build status
====================


<table>
    
  <tr>
    <td>Azure</td>
    <td>
      <details>
        <summary>
          <a href="https://dev.azure.com/tudat-team/feedstock-builds/_build/latest?definitionId=&branchName=master">
            <img src="https://dev.azure.com/tudat-team/feedstock-builds/_apis/build/status/feedstock-feedstock?branchName=master">
          </a>
        </summary>
        <table>
          <thead><tr><th>Variant</th><th>Status</th></tr></thead>
          <tbody><tr>
              <td>linux_64</td>
              <td>
                <a href="https://dev.azure.com/tudat-team/feedstock-builds/_build/latest?definitionId=&branchName=master">
                  <img src="https://dev.azure.com/tudat-team/feedstock-builds/_apis/build/status/feedstock-feedstock?branchName=master&jobName=linux&configuration=linux_64_" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>osx_64</td>
              <td>
                <a href="https://dev.azure.com/tudat-team/feedstock-builds/_build/latest?definitionId=&branchName=master">
                  <img src="https://dev.azure.com/tudat-team/feedstock-builds/_apis/build/status/feedstock-feedstock?branchName=master&jobName=osx&configuration=osx_64_" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>osx_arm64</td>
              <td>
                <a href="https://dev.azure.com/tudat-team/feedstock-builds/_build/latest?definitionId=&branchName=master">
                  <img src="https://dev.azure.com/tudat-team/feedstock-builds/_apis/build/status/feedstock-feedstock?branchName=master&jobName=osx&configuration=osx_arm64_" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>win_64</td>
              <td>
                <a href="https://dev.azure.com/tudat-team/feedstock-builds/_build/latest?definitionId=&branchName=master">
                  <img src="https://dev.azure.com/tudat-team/feedstock-builds/_apis/build/status/feedstock-feedstock?branchName=master&jobName=win&configuration=win_64_" alt="variant">
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </details>
    </td>
  </tr>
</table>

Current release info
====================

| Name | Downloads | Version | Platforms |
| --- | --- | --- | --- |
| [![Conda Recipe](https://img.shields.io/badge/recipe-nrlmsise--00-green.svg)](https://anaconda.org/tudat-team/nrlmsise-00) | [![Conda Downloads](https://img.shields.io/conda/dn/tudat-team/nrlmsise-00.svg)](https://anaconda.org/tudat-team/nrlmsise-00) | [![Conda Version](https://img.shields.io/conda/vn/tudat-team/nrlmsise-00.svg)](https://anaconda.org/tudat-team/nrlmsise-00) | [![Conda Platforms](https://img.shields.io/conda/pn/tudat-team/nrlmsise-00.svg)](https://anaconda.org/tudat-team/nrlmsise-00) |

Installing nrlmsise-00
======================

Installing `nrlmsise-00` from the `tudat-team` channel can be achieved by adding `tudat-team` to your channels with:

```
conda config --add channels tudat-team
conda config --set channel_priority strict
```

Once the `tudat-team` channel has been enabled, `nrlmsise-00` can be installed with:

```
conda install nrlmsise-00
```

It is possible to list all of the versions of `nrlmsise-00` available on your platform with:

```
conda search nrlmsise-00 --channel tudat-team
```




Updating nrlmsise-00-feedstock
==============================

If you would like to improve the nrlmsise-00 recipe or build a new
package version, please fork this repository and submit a PR. Upon submission,
your changes will be run on the appropriate platforms to give the reviewer an
opportunity to confirm that the changes result in a successful build. Once
merged, the recipe will be re-built and uploaded automatically to the
`tudat-team` channel, whereupon the built conda packages will be available for
everybody to install and use from the `tudat-team` channel.
Note that all branches in the tudat-team/nrlmsise-00-feedstock are
immediately built and any created packages are uploaded, so PRs should be based
on branches in forks and branches in the main repository should only be used to
build distinct package versions.

In order to produce a uniquely identifiable distribution:
 * If the version of a package **is not** being increased, please add or increase
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string).
 * If the version of a package **is** being increased, please remember to return
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string)
   back to 0.

Feedstock Maintainers
=====================


