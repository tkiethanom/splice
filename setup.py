from setuptools import setup, find_packages

setup(
    name="splice",
    version="1.1.33",
    description="Link authoring tool for " +
                "Firefox Directory and Enhanced Tiles",
    author="Mozilla",
    packages=find_packages(),
    include_package_data=True,
    scripts=["scripts/manage.py", "scripts/tile_index_crawl.py", "scripts/rs_to_pg.py"],
)
