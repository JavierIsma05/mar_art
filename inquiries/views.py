from urllib.parse import quote

from django.contrib import messages
from django.shortcuts import render

from .forms import InquiryForm


def contact(request):
    """Pagina de cotizacion con formulario."""
    whatsapp_message = ''

    if request.method == 'POST':
        form = InquiryForm(request.POST, request.FILES)
        if form.is_valid():
            inquiry = form.save()
            whatsapp_message = quote(
                f"Hola, quiero cotizar un producto personalizado.\n"
                f"Nombre: {inquiry.full_name}\n"
                f"WhatsApp: {inquiry.whatsapp}\n"
                f"Producto: {inquiry.get_service_interest_display()}\n"
                f"Cantidad: {inquiry.quantity}\n"
                f"Fecha requerida: {inquiry.needed_date or 'Por definir'}\n"
                f"Idea: {inquiry.message}"
            )
            messages.success(request, 'Tu solicitud fue guardada. Tambien puedes enviarla por WhatsApp.')
    else:
        initial = {}
        product_slug = request.GET.get('producto')
        if product_slug:
            initial['message'] = f"Quiero cotizar el producto: {product_slug}."
        form = InquiryForm(initial=initial)

    context = {
        'form': form,
        'whatsapp_message': whatsapp_message,
    }
    return render(request, 'public/contact.html', context)
