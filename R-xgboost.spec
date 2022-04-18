#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-xgboost
Version  : 1.6.0.1
Release  : 5
URL      : https://cran.r-project.org/src/contrib/xgboost_1.6.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/xgboost_1.6.0.1.tar.gz
Summary  : Extreme Gradient Boosting
Group    : Development/Tools
License  : Apache-2.0
Requires: R-xgboost-lib = %{version}-%{release}
Requires: R-data.table
Requires: R-jsonlite
BuildRequires : R-data.table
BuildRequires : R-jsonlite
BuildRequires : buildreq-R
BuildRequires : buildreq-cmake

%description
No detailed description available

%package lib
Summary: lib components for the R-xgboost package.
Group: Libraries

%description lib
lib components for the R-xgboost package.


%prep
%setup -q -c -n xgboost
cd %{_builddir}/xgboost

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650298779

%install
export SOURCE_DATE_EPOCH=1650298779
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xgboost
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xgboost
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xgboost
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc xgboost || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/xgboost/DESCRIPTION
/usr/lib64/R/library/xgboost/INDEX
/usr/lib64/R/library/xgboost/LICENSE
/usr/lib64/R/library/xgboost/Meta/Rd.rds
/usr/lib64/R/library/xgboost/Meta/data.rds
/usr/lib64/R/library/xgboost/Meta/demo.rds
/usr/lib64/R/library/xgboost/Meta/features.rds
/usr/lib64/R/library/xgboost/Meta/hsearch.rds
/usr/lib64/R/library/xgboost/Meta/links.rds
/usr/lib64/R/library/xgboost/Meta/nsInfo.rds
/usr/lib64/R/library/xgboost/Meta/package.rds
/usr/lib64/R/library/xgboost/Meta/vignette.rds
/usr/lib64/R/library/xgboost/NAMESPACE
/usr/lib64/R/library/xgboost/R/xgboost
/usr/lib64/R/library/xgboost/R/xgboost.rdb
/usr/lib64/R/library/xgboost/R/xgboost.rdx
/usr/lib64/R/library/xgboost/data/agaricus.test.rda
/usr/lib64/R/library/xgboost/data/agaricus.train.rda
/usr/lib64/R/library/xgboost/demo/basic_walkthrough.R
/usr/lib64/R/library/xgboost/demo/boost_from_prediction.R
/usr/lib64/R/library/xgboost/demo/caret_wrapper.R
/usr/lib64/R/library/xgboost/demo/create_sparse_matrix.R
/usr/lib64/R/library/xgboost/demo/cross_validation.R
/usr/lib64/R/library/xgboost/demo/custom_objective.R
/usr/lib64/R/library/xgboost/demo/early_stopping.R
/usr/lib64/R/library/xgboost/demo/generalized_linear_model.R
/usr/lib64/R/library/xgboost/demo/gpu_accelerated.R
/usr/lib64/R/library/xgboost/demo/interaction_constraints.R
/usr/lib64/R/library/xgboost/demo/poisson_regression.R
/usr/lib64/R/library/xgboost/demo/predict_first_ntree.R
/usr/lib64/R/library/xgboost/demo/predict_leaf_indices.R
/usr/lib64/R/library/xgboost/demo/tweedie_regression.R
/usr/lib64/R/library/xgboost/doc/discoverYourData.R
/usr/lib64/R/library/xgboost/doc/discoverYourData.Rmd
/usr/lib64/R/library/xgboost/doc/discoverYourData.html
/usr/lib64/R/library/xgboost/doc/index.html
/usr/lib64/R/library/xgboost/doc/xgboost.R
/usr/lib64/R/library/xgboost/doc/xgboost.Rnw
/usr/lib64/R/library/xgboost/doc/xgboost.pdf
/usr/lib64/R/library/xgboost/doc/xgboostPresentation.R
/usr/lib64/R/library/xgboost/doc/xgboostPresentation.Rmd
/usr/lib64/R/library/xgboost/doc/xgboostPresentation.html
/usr/lib64/R/library/xgboost/doc/xgboostfromJSON.R
/usr/lib64/R/library/xgboost/doc/xgboostfromJSON.Rmd
/usr/lib64/R/library/xgboost/doc/xgboostfromJSON.html
/usr/lib64/R/library/xgboost/help/AnIndex
/usr/lib64/R/library/xgboost/help/aliases.rds
/usr/lib64/R/library/xgboost/help/paths.rds
/usr/lib64/R/library/xgboost/help/xgboost.rdb
/usr/lib64/R/library/xgboost/help/xgboost.rdx
/usr/lib64/R/library/xgboost/html/00Index.html
/usr/lib64/R/library/xgboost/html/R.css
/usr/lib64/R/library/xgboost/make-r-def.R
/usr/lib64/R/library/xgboost/tests/testthat.R
/usr/lib64/R/library/xgboost/tests/testthat/test_basic.R
/usr/lib64/R/library/xgboost/tests/testthat/test_callbacks.R
/usr/lib64/R/library/xgboost/tests/testthat/test_config.R
/usr/lib64/R/library/xgboost/tests/testthat/test_custom_objective.R
/usr/lib64/R/library/xgboost/tests/testthat/test_dmatrix.R
/usr/lib64/R/library/xgboost/tests/testthat/test_feature_weights.R
/usr/lib64/R/library/xgboost/tests/testthat/test_gc_safety.R
/usr/lib64/R/library/xgboost/tests/testthat/test_glm.R
/usr/lib64/R/library/xgboost/tests/testthat/test_helpers.R
/usr/lib64/R/library/xgboost/tests/testthat/test_interaction_constraints.R
/usr/lib64/R/library/xgboost/tests/testthat/test_interactions.R
/usr/lib64/R/library/xgboost/tests/testthat/test_io.R
/usr/lib64/R/library/xgboost/tests/testthat/test_model_compatibility.R
/usr/lib64/R/library/xgboost/tests/testthat/test_monotone.R
/usr/lib64/R/library/xgboost/tests/testthat/test_parameter_exposure.R
/usr/lib64/R/library/xgboost/tests/testthat/test_poisson_regression.R
/usr/lib64/R/library/xgboost/tests/testthat/test_ranking.R
/usr/lib64/R/library/xgboost/tests/testthat/test_update.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/xgboost/libs/xgboost.so
/usr/lib64/R/library/xgboost/libs/xgboost.so.avx2
/usr/lib64/R/library/xgboost/libs/xgboost.so.avx512
