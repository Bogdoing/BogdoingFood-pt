class cards:
    card_modal = "700 грамм муки Twins Chakra Flour, 300 г муки Blue Triangle, 15 грамм растворимых дрожжей"

    def split_card_modal():
        return cards.card_modal.split(', ')
    
    card_modal_split = split_card_modal()

    card = {
        "card-title": "card-title",
        "card-text": "card-text",
        "card_img": "card_img",
        
        "modal_body": "modal_body",
        "madal_id": "madal_id",
        "card_modal" : card_modal_split, 
    }

    card2 = {
        "card-title2": "card-title2",
        "card-text": "card-text",
        "card_img": "card_img",
        
        "modal_body": "modal_body",
        "madal_id": "madal_id",
        "card_modal" : card_modal_split, 
    }

    cards = [card, card2] 
