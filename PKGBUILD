# Maintainer: Aster <asterlenist.channel@gmail.com>
pkgname=reper
pkgver=0.1
pkgrel=1
pkgdesc="CLI программа для проверки репутации пакетов на Arch Linux"
arch=('x86_64')
url="https://github.com/Asterlenist/gilza-reper"
license=('MIT')
depends=('python')
source=("reper.py")
sha256sums=('SKIP')  # для прототипа, потом ставь хеш

package() {
    install -Dm755 reper.py "$pkgdir/usr/bin/gilza-reper"
}
