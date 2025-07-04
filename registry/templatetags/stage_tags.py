from django import template
from ..models import InvestmentStage, InvestorType, SupportProgramType 

register = template.Library()

@register.simple_tag
def get_all_stages():
    return InvestmentStage.objects.all()


@register.simple_tag
def get_all_investor_types():
    return InvestorType.objects.all()


@register.simple_tag
def get_all_support_program_types():
    return SupportProgramType.objects.all()


from django.template.defaultfilters import floatformat

@register.filter
def humanize_currency(value, currency_code="USD"):
    """
    Converts a number to a human-readable currency format (e.g., 100000 as USD 100k).
    """
    try:
        value = float(value)
    except (ValueError, TypeError):
        return value  # Return original value if not a valid number

    if value >= 1_000_000_000_000:
        formatted_value = floatformat(value / 1_000_000_000_000, 1) + "T"
    elif value >= 1_000_000_000:
        formatted_value = floatformat(value / 1_000_000_000, 1) + "B"
    elif value >= 1_000_000:
        formatted_value = floatformat(value / 1_000_000, 1) + "M"
    elif value >= 1_000:
        formatted_value = floatformat(value / 1_000, 1) + "k"
    else:
        return f"{currency_code} {value:,.0f}"  # Format smaller numbers with comma

    return f"{currency_code} {formatted_value}"