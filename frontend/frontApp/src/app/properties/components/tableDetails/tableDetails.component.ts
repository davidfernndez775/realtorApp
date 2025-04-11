import { ChangeDetectionStrategy, Component } from '@angular/core';
import { DecimalPipe } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {
  NgbPaginationModule,
  NgbTypeaheadModule,
} from '@ng-bootstrap/ng-bootstrap';

interface Country {
  name: string;
  area: number;
}

const COUNTRIES: Country[] = [
  {
    name: 'Russia',
    area: 17075200,
  },
  {
    name: 'France',
    area: 640679,
  },
  {
    name: 'Germany',
    area: 357114,
  },
  {
    name: 'Portugal',
    area: 92090,
  },
  {
    name: 'Canada',
    area: 9976140,
  },
  {
    name: 'Vietnam',
    area: 331212,
  },
  {
    name: 'Brazil',
    area: 8515767,
  },
  {
    name: 'Mexico',
    area: 1964375,
  },
  {
    name: 'United States',
    area: 9629091,
  },
  {
    name: 'India',
    area: 3287263,
  },
  {
    name: 'Indonesia',
    area: 1910931,
  },
  {
    name: 'Tuvalu',
    area: 26,
  },
  {
    name: 'China',
    area: 9596960,
  },
];

@Component({
  selector: 'app-table-details',
  standalone: true,
  imports: [DecimalPipe, FormsModule, NgbTypeaheadModule, NgbPaginationModule],
  templateUrl: './tableDetails.component.html',
  styleUrl: './tableDetails.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class TableDetailsComponent {
  page = 1;
  pageSize = 4;
  collectionSize = COUNTRIES.length;
  countries: Country[] = [];

  constructor() {
    this.refreshCountries();
  }

  refreshCountries() {
    this.countries = COUNTRIES.map((country, i) => ({
      id: i + 1,
      ...country,
    })).slice(
      (this.page - 1) * this.pageSize,
      (this.page - 1) * this.pageSize + this.pageSize
    );
  }
}
