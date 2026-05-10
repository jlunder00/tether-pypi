
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".github"))
from actions import main as github_action


def execute_register(pkg_name, version, author, short_desc, homepage):
    os.environ["PKG_ACTION"] = "REGISTER"
    os.environ["PKG_NAME"] = pkg_name
    os.environ["PKG_VERSION"] = version
    os.environ["PKG_AUTHOR"] = author
    os.environ["PKG_SHORT_DESC"] = short_desc
    os.environ["PKG_HOMEPAGE"] = homepage
    github_action()
    print(f"Package {pkg_name} registered at {version}")


if __name__ == "__main__":
    # tether-premium: private repo, requires GitHub token to install.
    # v0.0.0 is a placeholder — no tag exists yet. Real versions are added
    # automatically via update.yml when scripts/release.sh runs in tether-premium.
    execute_register(
        pkg_name="tether-premium",
        version="v0.0.0",
        author="Jason Lunder",
        short_desc="Premium AI assistant features for Tether (private, token required to install)",
        homepage="https://github.com/jlunder00/tether-premium",
    )
