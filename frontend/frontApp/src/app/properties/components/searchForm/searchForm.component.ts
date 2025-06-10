import {
  ChangeDetectionStrategy,
  Component,
  EventEmitter,
  inject,
  Input,
  Output,
  TemplateRef,
  ViewEncapsulation,
} from '@angular/core';
import { NgbOffcanvas } from '@ng-bootstrap/ng-bootstrap';
import { NgbDropdownModule } from '@ng-bootstrap/ng-bootstrap';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { RealEstateProperty } from '../../interfaces/realEstatePropertyinterface.';
import { CommonModule } from '@angular/common';
import { NgbActiveOffcanvas } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-search-form',
  standalone: true,
  imports: [CommonModule, NgbDropdownModule, ReactiveFormsModule],
  templateUrl: './searchForm.component.html',
  styleUrl: './searchForm.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
  encapsulation: ViewEncapsulation.None,
})
export class SearchFormComponent {
  private offcanvasService = inject(NgbOffcanvas);

  counties = [
    'Broward',
    'Charlotte',
    'Collier',
    'Glades',
    'Hendry',
    'Highlands',
    'Lee',
    'Martin',
    'Miami Dade',
    'Monroe',
    'Okeechobee',
    'Palm Beach',
    'Saint Lucie',
  ];
  propertyTypes = [
    'Single Family',
    'Condo/Co-Op/Villa/Townhouse',
    'Multi-Family Income',
    'Residential Land/Boat Docks',
    'Land-Commercial/Business/Agricultural/Industrial',
    'Residential Rental',
    'Commercial/Industrial',
    'Business Brokerage',
  ];

  @Output() filtersApplied = new EventEmitter<any>();

  filterForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.filterForm = this.fb.group({
      property_type: [''],
      county: [''],
      for_rent_or_sale: [''],
      new: [false],
      price_decrease: [false],
      water_front: [false],
      price_min: [null],
      price_max: [null],
      square_ft_min: [null],
      square_ft_max: [null],
      beds_min: [null],
      beds_max: [null],
      full_baths_min: [null],
      full_baths_max: [null],
      half_baths_min: [null],
      half_baths_max: [null],
      built_min: [null],
      built_max: [null],
    });
  }

  get filterKeys(): string[] {
    return Object.keys(this.filterForm.controls);
  }

  openEnd(content: TemplateRef<any>) {
    this.offcanvasService.open(content, { position: 'end' });
  }

  onSubmit(offcanvas: NgbActiveOffcanvas): void {
    this.applyFilters();
    offcanvas.close('Submit/Enter key');
  }

  applyFilters(): void {
    this.filtersApplied.emit(this.filterForm.value);
  }

  getLabel(key: string): string {
    const map: Record<string, string> = {
      property_type: 'Type',
      county: 'County',
      for_rent_or_sale: 'Listing',
      new: 'New',
      price_decrease: 'Price ↓',
      water_front: 'Waterfront',
      price_min: 'Min Price',
      price_max: 'Max Price',
      square_ft_min: 'Min SqFt',
      square_ft_max: 'Max SqFt',
      beds_min: 'Min Beds',
      beds_max: 'Max Beds',
      full_baths_min: 'Min Full Baths',
      full_baths_max: 'Max Full Baths',
      half_baths_min: 'Min Half Baths',
      half_baths_max: 'Max Half Baths',
      built_min: 'Built From',
      built_max: 'Built To',
    };
    return map[key] || key;
  }

  hasValue(key: string): boolean {
    const val = this.filterForm.get(key)?.value;
    return (
      val !== null && val !== '' && !(typeof val === 'boolean' && val === false)
    );
  }

  getValue(key: string): any {
    const val = this.filterForm.get(key)?.value;
    if (typeof val === 'boolean') return val ? 'Yes' : '';
    return val;
  }

  removeFilter(key: string): void {
    const control = this.filterForm.get(key);
    if (control) {
      control.reset(control.value instanceof Boolean ? false : '');
      this.applyFilters(); // re-emite con el nuevo filtro
    }
  }
}
