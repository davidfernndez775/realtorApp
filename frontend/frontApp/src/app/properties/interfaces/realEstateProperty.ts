export interface RealEstateProperty {
  id: number;
  title: string;
  lon: string;
  lat: string;
  county: string;
  address: string;
  property_type: string;
  zip_code: number;
  for_rent_or_sale: string;
  price: number;
  square_ft: number;
  beds: number;
  full_baths: number;
  half_baths: number;
  built: number;
  description: string;
  new: boolean;
  price_decrease: boolean;
  water_front: boolean;
  main_image: string;
}
