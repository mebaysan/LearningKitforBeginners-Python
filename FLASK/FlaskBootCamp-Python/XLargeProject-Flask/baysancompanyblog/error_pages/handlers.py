from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)


# error_pages adlı blueprintimize flask ile otomatik gelen app_errorhandler methodu ile 404 sayfaları için bir hata yakalama operasyonu yaptık
@error_pages.app_errorhandler(404)
def error_404(error):  # method bir error alıyor
    # return ederken 404'ü de return ediyoruz
    # error_pages klasörü altındaki 404.html'i döndürür
    return render_template('error_pages/404.html'), 404


@error_pages.app_errorhandler(403)
def error_403(error): 
    return render_template('error_pages/403.html'), 403
