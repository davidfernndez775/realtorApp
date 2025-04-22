export interface RealEstatePropertyList {
  id: number;
  title: string;
  lon: string;
  lat: string;
  county: string;
  property_type: string;
  for_rent_or_sale: string;
  price: number;
  square_ft: number;
  beds: number;
  new: boolean;
  price_decrease: boolean;
  water_front: boolean;
  main_image: string;
}
